from model.date_prices import DatePrices
import reflex as rx
from typing import Union


def save_data(day, prices, colors):
    result = get_data(day=day)
    if not result:
        with rx.session() as session:
            session.add( DatePrices(colors=colors, prices=prices, day=day))
            session.commit()
                    
    else:
        update_data(day, prices, colors)
            
                       

def update_data(day, prices, colors):
    with rx.session() as session:

        p = session.exec(DatePrices.select().where(DatePrices.day == day)).first()
        p.prices = prices
        p.colors = colors

        session.add(p)
        session.commit()
        session.refresh(p)


def get_data(day)->DatePrices:
    with rx.session() as session:
        result = session.exec(DatePrices.select().where(DatePrices.day == day)).first()

        return result
    
