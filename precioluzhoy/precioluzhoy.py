from render_prices import render_prices, State
import reflex as rx

@rx.page("/", on_load= State.load_data)
def index() -> rx.Component:
    return  render_prices()
    


app = rx.App(
      stylesheets=[ "/css/animations.css"]  
)
app.add_page(index)









