def clean_symbols_with_user_input_and_default():
    symbols_string = input("Enter a list of symbols separated by commas (press Enter to skip): ")
    symbols = []

    if symbols_string:
        symbols = symbols_string.strip().split(",")
    else:
        symbols = ["AAVEUSDT", "STXUSDT", "ARBUSDT"]

    symbols = clean_symbols(symbols)
    symbols = upper_symbols(symbols)
    return symbols

def clean_symbols(symbols):
    return [symbol.strip() for symbol in symbols]

def upper_symbols(symbols):
    return [symbol.upper() for symbol in symbols]
