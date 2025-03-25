from utils import update_prices
from datetime import  date, datetime,timezone
import reflex as rx
import pytz
import db_manager
from model.date_prices import DatePrices
from typing import Optional

DAY_TIME_PERIOD = ["00:00 - 01:00", "01:00 - 02:00", "02:00 - 03:00", "03:00 - 04:00", "04:00 - 05:00", "05:00 - 06:00", "06:00 - 07:00", "07:00 - 08:00", "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00", "21:00 - 22:00", "22:00 - 23:00", "23:00 - 24:00"]

DAY_TIME = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', 
 '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', 
 '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']


class State(rx.State):
    
    today_prices: Optional[DatePrices] = None
    tomorrow_prices: Optional[DatePrices] = None
    color_list: list
    clock_icon_list: list
    day_hour: str
    date_now: datetime = datetime.now(timezone.utc)
    date: str
    today: bool
    tomorrow: bool
    hide_tomorrow: bool

    @rx.event
    def update(self):
        paris_tz = pytz.timezone("Europe/Paris")
        self.date_now = datetime.now(paris_tz)

    def load_data(self):
        paris_tz = pytz.timezone("Europe/Paris")
        self.date_now = datetime.now(paris_tz)

        prices, color_list =  update_prices()
        self.color_list = color_list

        self.clock_icon_list = []
        self.color_list = []
        
        self.date = str(date.today())
        self.day_hour = str(self.date_now)[11:13] + ":00"


        for i in DAY_TIME:
            if i == self.day_hour:
                self.clock_icon_list.append(True)
            else:
                self.clock_icon_list.append(False)

        if "today" in prices:
            db_manager.save_data("today", prices["today"], color_list)
            self.hide_tomorrow = False

        if "tomorrow" in prices:
            db_manager.save_data("tomorrow", prices["tomorrow"], color_list)
            self.hide_tomorrow = True

        self.today_prices = db_manager.get_data("today")
        self.tomorrow_prices = db_manager.get_data("tomorrow")

        return rx.scroll_to(elem_id="focus")


def render_prices()->rx.Component:
    return rx.vstack(
rx.vstack(
            rx.vstack(rx.text("Precio de la luz hoy", align="center", font_size = "30px", color = "black", margin_top = "30px"),
            rx.text(State.date,  align="center",font_size = "20px", color = "black"),
            rx.moment(State.date_now, interval=1000,format="HH:mm:ss" , tz="Europe/Paris", on_change= State.update, color = "black"),
            rx.text("Tarifa PVPC. Fuente: Red Eléctrica Española", align="center", font_size = "12px", color = "black"),
            rx.spacer(),
            rx.flex(
            rx.vstack(rx.foreach(DAY_TIME_PERIOD, 
                                 lambda x, i: rx.hstack(    
                                        rx.icon("clock-2",  color = f"rgb{State.today_prices.colors[i]}"),
                                                        
                                                rx.cond(State.clock_icon_list[i],  
                                                        rx.text(x,white_space ="nowrap",
                                                                color = "black",
                                                                font_weight = "900",
                                                                font_size = "17px",
                                                                    animation = "thumbs 1.5s",
                                                                    id = "focus"),
                                                rx.text(x,white_space ="nowrap", color = "black"))
                                                        )
                                        ),                                      
                        align= "start", ),
            
            rx.vstack(rx.foreach(State.today_prices.prices, 
                                 lambda x, i: rx.cond(State.clock_icon_list[i],
                                                            rx.text(f"{x} €/kWh", 
                                                            color = f"rgb{State.today_prices.colors[i]}",
                                                            white_space ="nowrap",
                                                            font_size = "17px",
                                                            font_weight = "bold",
                                                            animation = "thumbs 1.5s"),
                                                            rx.text(f"{x} €/kWh", 
                                                            color = f"rgb{State.today_prices.colors[i]}",
                                                            white_space ="nowrap",
                                                            ))),
                                                            
                            align= "end"),
                        
                        align="center",
                        justify="between",
                        bg = "#edf9ff",
                        min_width = "350px",
                        flex_grow = "3",
                        padding = "30px",
                        animation = "fadeDown 0.5s ease-in-out;",
                        border = "2px solid #3498db",
                        border_radius = "12px",
                        margin_bottom = "30px"
                    
            
                    ), 
                    rx.spacer(),
                    align="center"),
                    
                    align="center",
                    bg = "white",
                    ),

rx.cond(State.hide_tomorrow, rx.vstack(
            rx.vstack(rx.text("Precio de la luz mañana", align="center", font_size = "30px", color = "black", margin_top = "30px"),
            rx.moment(State.date_now, interval=1000,format="HH:mm:ss" , tz="Europe/Paris", on_change= State.update),
            rx.text("Tarifa PVPC. Fuente: Red Eléctrica Española", align="center", font_size = "12px", color = "black"),
            rx.spacer(),
            rx.flex(
            rx.vstack(rx.foreach(DAY_TIME_PERIOD, 
                                 lambda x, i: rx.hstack(    
                                        rx.icon("clock-2",  color = f"rgb{State.tomorrow_prices.colors[i]}"),
                                                        
                                                rx.cond(State.clock_icon_list[i],  
                                                        rx.text(x,white_space ="nowrap",
                                                                color = "black",
                                                                font_weight = "900",
                                                                font_size = "17px",
                                                                    animation = "thumbs 1.5s",
                                                                    ),
                                                rx.text(x,white_space ="nowrap", color = "black"))
                                                        )
                                        ),                                      
                        align= "start", ),
            
            rx.vstack(rx.foreach(State.tomorrow_prices.prices, 
                                 lambda x, i: rx.cond(State.clock_icon_list[i],
                                                            rx.text(f"{x} €/kWh", 
                                                            color = f"rgb{State.tomorrow_prices.colors[i]}",
                                                            white_space ="nowrap",
                                                            font_size = "17px",
                                                            font_weight = "bold",
                                                            animation = "thumbs 1.5s"),
                                                            rx.text(f"{x} €/kWh", 
                                                            color = f"rgb{State.tomorrow_prices.colors[i]}",
                                                            white_space ="nowrap",
                                                            ))),
                                                            
                            align= "end"),
                        
                        align="center",
                        justify="between",
                        bg = "#edf9ff",
                        min_width = "350px",
                        flex_grow = "3",
                        padding = "30px",
                        animation = "fadeDown 0.5s ease-in-out;",
                        border = "2px solid #3498db",
                        border_radius = "12px",
                        margin_bottom = "30px"
                    
            
                    ), 
                    rx.spacer(),
                    align="center"),
                    
                    align="center",
              
                    on_mount= State.load_data)),
            align="center",
            bg = "white"


                    )





