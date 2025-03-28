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
        madrid_tz = pytz.timezone('Europe/Madrid')
        self.date_now = datetime.now(madrid_tz)
        if 0000 < int(self.date_now.strftime("%H%M")) < 1000:
            self.hide_tomorrow = False
        if self.date_now.second % 10 == 0 and self.date_now.strftime("%H") == "21" and self.hide_tomorrow == False:
            self.load_data()


    def load_data(self):
        madrid_tz = pytz.timezone('Europe/Madrid')
        self.date_now = datetime.now(madrid_tz)
        self.date = str(date.today())
        self.day_hour = str(self.date_now)[11:13] + ":00"
        self.clock_icon_list = []

        res = db_manager.get_all()
        for i in res: print(i.date)

        for i in DAY_TIME:
            if i == self.day_hour:
                self.clock_icon_list.append(True)
            else:
                self.clock_icon_list.append(False)

        prices, color_list, file_date =  update_prices()
        db_manager.save_data(file_date, prices, color_list)

        if self.date == file_date:
            self.today_prices = db_manager.get_data(file_date)
            self.hide_tomorrow = False
        elif self.date < file_date:
            self.tomorrow_prices =db_manager.get_data(file_date)
            self.today_prices = db_manager.get_data(self.date)
            self.hide_tomorrow = True

        return rx.scroll_to(elem_id="focus_item_id")


    def delete(self):
        db_manager.delete()


def render_prices()->rx.Component:
    return rx.cond(State.is_hydrated, rx.vstack(
        #rx.button("Delete", on_click=State.delete),
    rx.vstack(
            rx.vstack(rx.text("Precio de la luz hoy", align="center", font_size = "20px", color = "black", margin_top = "10px"),
            rx.text(State.today_prices.date,  align="center", font_size = "15px", color = "black"),
            rx.moment(State.date_now, interval=1000,format="HH:mm:ss" , tz="Europe/Paris",font_size = "15px", on_change= State.update, color = "black"),
            rx.text("Tarifa PVPC. Fuente: Red Eléctrica Española", align="center", font_size = "12px", color = "black"),
            rx.spacer(),
            rx.flex(
            rx.vstack(rx.foreach(DAY_TIME_PERIOD, 
                                 lambda x, i: rx.hstack(    
                                        rx.icon("clock-2",  color = f"{State.today_prices.colors[i]}"),
                                                        
                                                rx.cond(State.clock_icon_list[i],  
                                                        rx.text(x,white_space ="nowrap", color = "black", font_weight = "900",
                                                                font_size = "17px", animation = "thumbs 1.5s", id = "focus_item_id"),                                                                                     
                                                        rx.text(x,white_space ="nowrap", color = "black"))
                                                        )
                                        ),                                      
                        align= "start"),
            
            rx.vstack(rx.foreach(State.today_prices.prices, 
                                 lambda x, i: rx.cond(State.clock_icon_list[i],
                                                            rx.text(f"{x} €/kWh", color = f"{State.today_prices.colors[i]}", white_space ="nowrap", 
                                                                     font_size = "17px",font_weight = "900",animation = "thumbs 1.5s"),
                                                            rx.text(f"{x} €/kWh", color = f"{State.today_prices.colors[i]}", white_space ="nowrap",
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
                rx.vstack(rx.text("Precio de la luz mañana", align="center", font_size = "20px", color = "black", margin_top = "10px"),
                          rx.text(State.tomorrow_prices.date,  align="center",font_size = "15px", color = "black"),
                #rx.moment(State.date_now, interval=1000,format="HH:mm:ss" ,font_size = "15px", tz="Europe/Paris", on_change= State.update),
                rx.text("Tarifa PVPC. Fuente: Red Eléctrica Española", align="center", font_size = "12px", color = "black"),
        
                rx.flex(
                rx.vstack(rx.foreach(DAY_TIME_PERIOD, 
                                    lambda x, i: rx.hstack(    
                                            rx.icon("clock-2",  color = f"{State.tomorrow_prices.colors[i]}"),
                                                            
                                                    rx.cond(State.clock_icon_list[i],  
                                                            rx.text(x,white_space ="nowrap",
                                                                    color = "black",
                                                                    ),
                                                    rx.text(x,white_space ="nowrap", color = "black"))
                                                            )
                                    ),                                      
                    align= "start"),
                
                rx.vstack(rx.foreach(State.tomorrow_prices.prices, 
                                    lambda x, i: rx.cond(State.clock_icon_list[i],
                                                                rx.text(f"{x} €/kWh", 
                                                                color = f"{State.tomorrow_prices.colors[i]}",
                                                                white_space ="nowrap",
                                                                ),
                                                                rx.text(f"{x} €/kWh", 
                                                                color = f"{State.tomorrow_prices.colors[i]}",
                                                                white_space ="nowrap",
                                                                ))),
                                                                
                            align= "end"),
                            align="center",
                            justify="between",
                            bg = "#edf9ff",
                            min_width = "350px",
                            flex_grow = "3",
                            padding = "30px",
                            border = "2px solid #3498db",
                            border_radius = "12px",
                            margin_bottom = "30px"
                        ), 
                    
                        align="center"),
                        align="center",
                        )),
                align="center",
                bg = "white",
                on_mount=State.load_data


                        )
)




