import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import pandas as pd


def create_visualization_ohlc_ma_and_position(df, minutely_interval):
    # Get the minutely_interval to display
    df_dropna = df.dropna()

    # Get the data for the specified minutely_interval
    coin_data = df_dropna[df_dropna['minutelyInterval'] == minutely_interval]

    # Get the unique coins
    coins = coin_data['coin'].unique()

    # Loop over the coins and plot the MA50, MA100, MA200 and position for each coin
    for coin in coins:
        print(coin)
        coin_data_filtered = coin_data[coin_data['coin'] == coin]
        # Convert 'time' column to datetime format
        coin_data_filtered['time'] = pd.to_datetime(coin_data_filtered['time'])

        plt.figure(figsize=(12, 6))
        plt.plot(coin_data_filtered["time"], coin_data_filtered["open"], color="blue", linestyle=":", label="Open")
        plt.plot(coin_data_filtered["time"], coin_data_filtered["high"], color="red", linestyle=":", label="High")
        plt.plot(coin_data_filtered["time"], coin_data_filtered["low"], color="green", linestyle=":", label="Low")
        plt.plot(coin_data_filtered["time"], coin_data_filtered["close"], color="purple", linestyle=":", label="Close")
        plt.plot(coin_data_filtered["time"], coin_data_filtered["ma50"], color="blue", linestyle="-", label="MA50")
        plt.plot(coin_data_filtered["time"], coin_data_filtered["ma100"], color="red", linestyle="-.", label="MA100")
        plt.plot(coin_data_filtered['time'], coin_data_filtered['ma200'], color="green", linestyle="--", label="MA200")

        buy_positions = coin_data_filtered[coin_data_filtered["position"] == "BUY"]
        sell_positions = coin_data_filtered[coin_data_filtered["position"] == "SELL"]
        plt.scatter(buy_positions["time"], buy_positions["close"], marker="o", color="black", label="BUY", zorder=8)
        plt.scatter(sell_positions["time"], sell_positions["close"], marker="x", color="black", label="SELL", zorder=8)

        # Add labels and title
        # Formatting the x-axis with readable dates
        date_formatter = mdates.DateFormatter('%Y-%m-%d %H:%M')  # Customize the date format here
        plt.gca().xaxis.set_major_formatter(date_formatter)
        plt.gcf().autofmt_xdate()  # Automatically adjust date labels for readability
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title(f"OHLC Data with Technical Indicators ({coin} by {minutely_interval} minutely)")
        plt.legend()

        # Show the plot
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def create_visualization_ohlc_candle_stick(df, minutely_interval):
    # Get the minutely_interval to display
    df_dropna = df.dropna()

    # Get the data for the specified minutely_interval
    coin_data = df_dropna[df_dropna['minutelyInterval'] == minutely_interval]

    # Get the unique coins
    coins = coin_data['coin'].unique()

    # Loop over the coins and plot the MA50, MA100, MA200 and position for each coin
    for coin in coins:
        print(coin)
        coin_data_filtered = coin_data[coin_data['coin'] == coin]

        coin_data_filtered = coin_data_filtered[["time", "open", "high", "low", "close"]]
        coin_data_filtered['time'] = pd.to_datetime(coin_data_filtered['time'])

        # Set the Date column as the index
        coin_data_filtered.set_index('time', inplace=True)
        fig, axes = mpf.plot(coin_data_filtered, type='candle', style='charles', title=f"OHLC Candle Stick Chart ({coin} by {minutely_interval} minutely)", datetime_format='%Y-%m-%d %H:%M', returnfig=True, figsize=(12, 6))

        main_axis = axes[0]
        main_axis.set_ylabel('Price')
        main_axis.grid(True)
 
        mpf.show()