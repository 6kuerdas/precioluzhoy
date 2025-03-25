from render_prices import render_prices
import reflex as rx


def index() -> rx.Component:
    return  render_prices()
    


app = rx.App(
      stylesheets=[ "/css/animations.css"]  
)
app.add_page(index)









