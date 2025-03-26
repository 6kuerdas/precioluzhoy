from model.date_prices import DatePrices
import reflex as rx
from typing import Union


def save_data(day, prices, colors):
    result = get_data(day=day)
    if not result:
        with rx.session() as session:
            session.add( DatePrices(colors=colors, prices=prices, date=day))
            session.commit()

def get_data(day)->DatePrices | None:
    with rx.session() as session:
        result = session.exec(DatePrices.select().where(DatePrices.date == day)).first()
        if result:
            return result            
        else:
            return None           
        
def get_all()->list | None:
    with rx.session() as session:
        return session.exec(DatePrices.select()).all()    


def delete():
    with rx.session() as session:
        res = session.exec(DatePrices.select()).all()
        for r in res:
            session.delete(r)
        session.commit()
    
