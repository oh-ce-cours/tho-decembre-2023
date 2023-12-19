import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

plt.style.use('fivethirtyeight')

df = pd.read_csv(
    "https://blockchain.info/charts/market-price?"
    "address=&daysAverageString=1&format=csv"
    "&scale=0&showDataPoints=false&"
    "show_header=true&timespan=")

df.columns = ("date", "price")
df.date = pd.to_datetime(df.date)
df = df.set_index('date')
df["diff_price"] = df.price.diff()
df.plot()


def upsample():
    df_upsample = df.copy().resample("60min").asfreq()
    df_upsample = df_upsample.interpolate("quadratic")
    df_upsample.diff_price = df_upsample.price.diff()
    return df_upsample


def downsample():
    df_downsample = df.copy().resample("7d").asfreq()
    df_downsample.diff_price = df_downsample.price.diff()
    return df_downsample


def diff_plot(df):
    """Plotte les différence sur une sorte d'histogramme.
    Rouge si négatif, vert si positif
    """
    ax =df.diff_price[df.diff_price >= 0].plot(kind="bar", color="g")
    (-1*df.diff_price[df.diff_price < 0]).plot(kind="bar", color="r", ax=ax)
    plt.legend()
    plt.show()



def moving_avg(df):
    moving_2 = df.price.rolling(window=2, center=True).mean()
    moving_5 = df.price.rolling(window=5, center=True).mean()
    moving_10 = df.price.rolling(window=10, center=True).mean()

    moving_2.plot(label="2")
    moving_5.plot(label="5")
    moving_10.plot(label="10")

    plt.legend()
    plt.show()
