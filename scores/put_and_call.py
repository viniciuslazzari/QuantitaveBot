import requests

ATTRIBUTE_WEIGHT = 25

URL = 'https://opcoes.net.br/historico/liquidez/json'
PARAMS = dict(
    ativos = 'ABEV,B3SA,BBAS,BBDC,BOVA,IBOV,MGLU,PETR,VALE,VIIA,WEGE',
    grupamento = 'Mensal'
)

def return_put_and_call_score():
    resp = requests.get(url = URL, params = PARAMS)
    data = resp.json()

    put_call_ratios = data["data"]["put_Call_Ratio"]

    put_call_ratios = put_call_ratios[1:]

    ratios = []

    for date_values in put_call_ratios:
        date_values = date_values[1:]

        sum_of_ratios = 0
        
        for value in date_values[:-1]:
            sum_of_ratios += value[1]

        ratios.append(sum_of_ratios / 11)

    today_value = ratios.pop()

    position = 0

    for item in ratios:
        if item > today_value:
            position += 1

    score = (ATTRIBUTE_WEIGHT / len(ratios)) * position

    return score