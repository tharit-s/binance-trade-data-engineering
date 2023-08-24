## Setup

To setup this project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/tharit-s/binance-trade-data-engineering.git
```

2. Create a virtual environment:
```
python3 -m venv env
```

3. Activate the virtual environment:
```
source env/bin/activate
```

4. Install the dependencies:
```
pip install -r requirements.txt
```

5. Run the project:

- Data ingestion trade data from binance to the brzone folder
```
python -m src.zones.bronze.main
```
- Data transform trade data from the bronze fodler to the silver folder
```
python -m src.zones.silver.main
```
- Data transform trade data from the silver fodler to the gold folder
```
python -m src.zones.gold.main
```