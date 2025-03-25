import reflex as rx

config = rx.Config(
    app_name="precioluzhoy",
    db_url="sqlite:///reflex.db",

    cors_allowed_origins = ["https://precioluzhoy-nine.vercel.app/",
                            "https://precioluzhoy-production.up.railway.app",
                            
                            "http://localhost:3000"]
)