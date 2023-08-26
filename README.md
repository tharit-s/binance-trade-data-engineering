## Setup

To setup this project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/tharit-s/binance-trade-data-engineering.git
```

2. Go to the project root path:
```
cd binance-trade-data-engineering
```

3. Create a virtual environment:
```
python3 -m venv env
```

4. Activate the virtual environment:
```
source env/bin/activate
```

5. Install the dependencies:
```
pip install -r requirements.txt
```

## Run

To run this project, follow these steps:

1. Data ingestion trade data from binance to the brzone folder
```
python src/zones/bronze/main.py
```
- After running the `main.py` script in the `bronze` zone, you will be prompted to select an option:
    - Option1: **Enter** to skip and use the default
    - Option2: **Input** your own symbols separated by commas for a sample list: `AAVEUSDT,STXUSDT,ARBUSDT` and then **Enter** to continue

2. Data transform trade data from the bronze fodler to the silver folder
```
python src/zones/silver/main.py
```

3. Data transform trade data from the silver fodler to the gold folder
```
python src/zones/gold/main.py
```