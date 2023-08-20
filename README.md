# bitazza-assignment-de
Bitazza assignment for data engineer

# Action items
- self-learning websocket -> done
- try to get data from the binance client -> done
- try to use the `binance-connector-python` library -> done
    - how to generate api key: https://stackoverflow.com/questions/67376632/how-to-create-binance-test-api-key
- try to use git on github -> done
    - reset the password and use the api key instead
- design the data lakehouse zones from the assignment
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
- review the virtual environment
- write a document in README.md
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
└── silver
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
- `id`: The unique identifier for the trade.
- `price`: The price of the trade in USDT.
- `qty`: The quantity of BTC traded in the trade.
- `quoteQty`: The total USDT value of the trade.
- `time`: The timestamp of the trade in Unix epoch milliseconds.
- `isBuyerMaker`: Indicates whether the buyer was the maker of the trade (True) or the taker of the trade (False).
- `isBestMatch`: Indicates whether the trade was the best price available at the time (True) or not (False).
### Silver Zone
#### Transforming (Calculate Open, High, Low, Close, Volume)
- `open`: The opening price of the coin in the given minute.
- `high`: The highest price of the coin in the given minute.
- `low`: The lowest price of the coin in the given minute.
- `close`: The closing price of the coin in the given minute.
- `volume`: The volume of the coin traded in the given minute.
#### Transforming (Partition Minutely 1/5/15/30/60)
- `coin`: The name of the coin.
- `minute`: The minute of the day.
- `open`: The opening price of the coin in the given minute.
- `high`: The highest price of the coin in the given minute.
- `low`: The lowest price of the coin in the given minute.
- `close`: The closing price of the coin in the given minute.
- `volume`: The volume of the coin traded in the given minute.
### Gold Zone
#### Analysis (compare MA(50) and MA(100) for decision making)
- `coin`: The name of the coin.
- `minute`: The minute of the day.
- `ma_50`: The value of the MA(50) for the coin in the given minute.
- `ma_100`: The value of the MA(100) for the coin in the given minute.
- `ma_200`: The value of the MA(200) for the coin in the given minute.
- `position`: The position of the broker for the coin in the given minute (i.e., "buy" or "sell").

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