# Learning log
## Action items
- self-learning websocket -> done
- try to get data from the binance client -> done
- try to use the `binance-connector-python` library -> done
    - how to generate api key: https://stackoverflow.com/questions/67376632/how-to-create-binance-test-api-key
- try to use git on github -> done
    - reset the password and use the api key instead
- design the data lakehouse zones from the assignment -> done
    - bronze
        - get full load data via restful api
            - how to write a list of dictionaries into the local folder
            - which file types to store data
                - json file
            - should partition data or replace after rerun the full load ingestion
            - design the folder structure in bronze zone
            - design when the input as a list of multiple coins
        - get streaming data via websocket
    - silver
        - transform data
            - cleansing data
                - convert timezone?
            - design data model
                - required columns
                    - open
                    - high
                    - low
                    - close
                    - volume
                - identity columns
                    - time?
                    - id?
                    - period of 1/5/15/30/60 minutely (by UTC time)?
            - how to calculate the data 1/5/15/30/60 minutely (by UTC time)
            - design folder structure in silver zone
    - gold
        - analyze data
            - design folder structure in gold zone
            - how to calculate MA({day_period}) from the closed price
            - create a new column for storing the status to buy or sell with the MA conditions
- naming convention -> done
- design a diagram -> done
    -  ![diagram v1](./images/bitazza-diagram-v1.jpg)
- design a architect -> done
- design data medel in dbdiagram.io
- review the virtual environment -> done
- apply the virtual environment into the project -> done
- add a note.md to store my short note while implementing -> done
- write a document in README.md -> done
- notify an email for the intruction

## Full Load Data Ingestion
- Get 2 records of `AAVEUSDT` from Binance RESTful API
```
[
    {'id': 104388712, 'price': '56.21000000', 'qty': '0.24300000', 'quoteQty': '13.65903000', 'time': 1692433675009, 'isBuyerMaker': False, 'isBestMatch': True
    },
    {'id': 104388713, 'price': '56.22000000', 'qty': '0.30100000', 'quoteQty': '16.92222000', 'time': 1692433707250, 'isBuyerMaker': False, 'isBestMatch': True
    }
]
```

## Data Lakehouse Architect Design
### Folder structure
```
datalakehouse
├── bronze
│   ├── batch
│   │   ├── coin1.json
│   │   ├── coin2.json
│   └── streaming
├── silver
│   ├── batch
│   │   ├── coin1_minutely_1.csv
│   │   ├── coin1_minutely_5.csv
│   │   ├── coin1_minutely_15.csv
│   │   ├── coin1_minutely_30.csv
│   │   ├── coin1_minutely_60.csv
│   │   └── coin2_minutely_1.csv
│   │   └── coin2_minutely_5.csv
│   │   └── coin2_minutely_15.csv
│   │   └── coin2_minutely_30.csv
│   │   └── coin2_minutely_60.csv
│   └── streaming
└── gold
    ├── batch
    │   ├── coin1_minutely_1.csv
    │   ├── coin1_minutely_5.csv
    │   ├── coin1_minutely_15.csv
    │   ├── coin1_minutely_30.csv
    │   ├── coin1_minutely_60.csv
    │   └── coin2_minutely_1.csv
    │   └── coin2_minutely_5.csv
    │   └── coin2_minutely_15.csv
    │   └── coin2_minutely_30.csv
    │   └── coin2_minutely_60.csv
    └── streaming
```
## Data model
### Bronze Zone
#### Landing
- **id**: Unique identifier for the data entry
  - Example: 32492152

- **price**: Price of the item
  - Example: 1.00580000

- **qty**: Quantity of the item
  - Example: 400.00000000

- **quoteQty**: Quote quantity of the item
  - Example: 402.32000000

- **time**: Timestamp of the data entry
  - Example: 1692846186370

- **isBuyerMaker**: Indicates if the buyer is the maker of the trade
  - Example: false

- **isBestMatch**: Indicates if the trade is the best match
  - Example: true

### Silver Zone
#### Transforming (Calculate Open, High, Low, Close, Volume)
- **time**: Timestamp of the data entry
  - Example: 2023-08-24 03:00:00

- **open**: Opening price at the given time
  - Example: 1.0058

- **high**: Highest price within the time interval
  - Example: 1.0061

- **low**: Lowest price within the time interval
  - Example: 1.0056

- **close**: Closing price at the given time
  - Example: 1.0057

- **volume**: Volume of trading at the given time
  - Example: 734889.2000000001

- **filename**: Name of the JSON file containing related data
  - Example: ARBUSDT.json

- **coin**: Identifier for the specific coin or cryptocurrency
  - Example: ARBUSDT

- **minutelyInterval**: Interval of data collection (in minutes)
  - Example: 1, 5, 15, 30, 60

### Gold Zone
#### Analysis (compare MA(50) and MA(100) for decision making)
- **Index**: Unique identifier for the data entry
  - Example: 0

- **time**: Timestamp of the data entry
  - Example: 2023-08-24 03:03:00

- **open**: Opening price at the given time
  - Example: 1.0058

- **high**: Highest price within the time interval
  - Example: 1.0061

- **low**: Lowest price within the time interval
  - Example: 1.0056

- **close**: Closing price at the given time
  - Example: 1.0056

- **volume**: Volume of trading at the given time
  - Example: 677343.6000000001

- **filename**: Name of the JSON file containing related data
  - Example: ARBUSDT.json

- **coin**: Identifier for the specific coin or cryptocurrency
  - Example: ARBUSDT

- **minutelyInterval**: Interval of data collection (in minutes)
  - Example: 1, 5, 15, 30, 60

- **ma50**: 50-period Moving Average value
  - Example: 1.0056

- **ma100**: 100-period Moving Average value
  - Example: 1.0056

- **ma200**: 200-period Moving Average value
  - Example: 1.0056

- **position**: Our broker wants to buy and hold the asset by comarison between MA(low) and MA(high) when the MA(50) < MA(100), and sell to hold BUSD or USDT when MA(50) >= MA(100).
  - Example: SELL, BUY

## Structuring project
```
src
├── main
│   ├── __init__.py
│   └── main.py
└── zones
    ├── bronze
    │   ├── __init__.py
    │   └── bronze_module.py
    │   └── main.py
    ├── silver
    │   ├── __init__.py
    │   └── silver_module.py
    │   └── main.py
    └── gold
        ├── __init__.py
        └── gold_module.py
        └── main.py
```