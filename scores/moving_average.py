import pandas as pd

ATTRIBUTE_WEIGHT = 20
MOVING_AVERAGE_VALUE = 100

def return_moving_average_score():
    ibov = pd.read_csv("data/IBOV.csv", index_col = 'Date', parse_dates = True)
    
    ibov['MA'] = ibov['Close'].rolling(MOVING_AVERAGE_VALUE).mean()

    list_of_moving_averages = ibov.tail(MOVING_AVERAGE_VALUE)["Close"].to_list()

    today_value = list_of_moving_averages.pop()

    position = 0

    for item in list_of_moving_averages:
        if item < today_value:
            position += 1

    score = (ATTRIBUTE_WEIGHT / len(list_of_moving_averages)) * position

    return score