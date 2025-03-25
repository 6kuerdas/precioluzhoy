import reflex as rx

config = rx.Config(
    app_name="precioluzhoy",
    
    
    cors_allowed_origins = [
                            "https://precioluzhoy-production.up.railway.app",
                              "https://precioluzhoy-nine.vercel.app",
                            
                            "http://localhost:3000"]
                    )