from render_prices import render_prices, State
import reflex as rx

@rx.page("/", on_load= State.load_data)
def index() -> rx.Component:
    return  render_prices()
    


app = rx.App(
      stylesheets=[ "/css/animations.css"],

          head_components=[
    rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-JF4HTKKJ22"),
    rx.script(
        """
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments)};
                     gtag('js', new Date());

                gtag('config', 'G-JF4HTKKJ22');
                    """ 
                )]
)
app.add_page(index)









