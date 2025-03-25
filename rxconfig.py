import reflex as rx

config = rx.Config(
    app_name="precioluzhoy",
    
    api_url = "https://precioluzhoy-production.up.railway.app:8000",
    
    cors_allowed_origins = ["https://precioluzhoy-nine.vercel.app",
                            "https://precioluzhoy-production.up.railway.app",
                            
                            "http://localhost:3000"]
                    )