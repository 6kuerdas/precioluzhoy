import requests
from datetime import  date
import pandas as pd 
import reflex as rx


def update_prices()-> tuple[dict, list]:
    current_date = str(date.today())
    url = "https://api.esios.ree.es/archives/71/download?date_type=publicacion&end_date={}T23%3A59%3A59%2B00%3A00&locale=es&start_date={}T00%3A00%3A00%2B00%3A00".format(current_date, current_date)    
    response =  requests.get(url)
    print(response)

    f="PVPC_" + current_date + ".xls"

    outfile = rx.get_upload_dir() / f
    with outfile.open("wb") as file:
        file.write(response.content)
        
    data = pd.read_excel(outfile, skiprows=[0,1,2,3], usecols="A")
    check_date = data['Día'].tolist()
    check_date = str(check_date[0])
    check_date = str(check_date[0:10])

    data = pd.read_excel(outfile,skiprows=[0,1,2,3], usecols="E")
    prices=data['Término energía PVPC\nFEU = TEU + TCU\n€/MWh consumo'].tolist()

    prices = [round(i/1000,5) for i in prices]        

    colors = gen_colors(prices)

    if current_date == check_date:
        return {"today": prices}, colors

    if current_date < check_date:
        return {"tomorrow": prices}, colors
        
def gen_colors(prices) -> list:
    # Normalize prices between 0 and 1 for color mapping
    min_val = min(prices)
    max_val = max(prices)
    normalized = [(p - min_val) / (max_val - min_val) for p in prices]

    # Generate RGB colors (Darker Green to Amber to Red)
    colors = []
    for n in normalized:
        if n < 0.5:
            # Green to Amber (start with slightly darker green and add red)
            red = int(255 * (2 * n))  # Red increases from 0 to 255
            green = int(225 * (1 - 2 * n))  # Amber: Green decreases from 204 to 0
            blue = 0
        else:
            # Amber to Red (start with amber and add more red)
            red = 255  # Red is always 255
            green = int(214 * (2 - 2 * n))  # Green decreases from 204 to 0
            blue = 0

        colors.append(f"({red}, {green}, {blue})")

    return colors