import requests
from datetime import  date
import pandas as pd 
import reflex as rx
from pathlib import Path


def update_prices()-> tuple[dict, list, str]:
    current_date = str(date.today())
    url = "https://api.esios.ree.es/archives/71/download?date_type=publicacion&end_date={}T23%3A59%3A59%2B00%3A00&locale=es&start_date={}T00%3A00%3A00%2B00%3A00".format(current_date, current_date)    
    response =  requests.get(url)
    print(response)

    f = Path("PVPC_" + current_date + ".xls")


    with f.open("wb") as file:
        file.write(response.content)
        
    data = pd.read_excel(f, skiprows=[0,1,2,3], usecols="A")
    check_date = data['Día'].tolist()
    check_date = str(check_date[0])
    check_date = str(check_date[0:10])

    data = pd.read_excel(f,skiprows=[0,1,2,3], usecols="E")
    prices=data['Término energía PVPC\nFEU = TEU + TCU\n€/MWh consumo'].tolist()

    prices = [round(i/1000,3) for i in prices]        

    for i in prices: print(i)

    colors = gen_colors(prices)

    return prices, colors, check_date
        
def gen_colors(prices: list[float]) -> list[str]:
    if not prices:
        return []

    sorted_prices = sorted(prices)
    n = len(prices)

    low_cutoff = sorted_prices[int(n * 0.5)]
    high_cutoff = sorted_prices[int(n * 0.67)]

    return [
        "rgb(0, 190, 0)" if price <= low_cutoff else
        "rgb(255, 191, 0)" if price <= high_cutoff else
        "rgb(230, 0, 0)"
        for price in prices
    ]





