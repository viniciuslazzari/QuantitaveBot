import pandas as pd
import numpy as np

ATTRIBUTE_WEIGHT = 20

DAYS_VALUE = 40

def return_for_safe_heaven():
    selic = pd.read_csv("data/SELIC.csv", delimiter = ";")

    selic = selic.head(DAYS_VALUE)["Fator diário"].str.replace(',', '.').astype(float).to_list()

    rate = np.prod(selic)

    return rate

def return_for_market():
    ibov = pd.read_csv("data/IBOV.csv", index_col = 'Date', parse_dates = True)

    ibov = ibov.tail(DAYS_VALUE)

    first_day_index = ibov.iloc[0]["Open"]
    last_day_index = ibov.iloc[-1]["Close"]

    rate = last_day_index / first_day_index

    return rate

def return_safe_heaven_score():
    selic_rate = return_for_safe_heaven()
    market_rate = return_for_market()

    diff = (market_rate - selic_rate) * 100

    score = 0

    if diff >= 10:
        score = ATTRIBUTE_WEIGHT
    elif diff > -10:
        score = diff + 10

    return score