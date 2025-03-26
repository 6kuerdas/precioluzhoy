import reflex as rx

config = rx.Config(
    app_name="precioluzhoy",
    
    
    cors_allowed_origins = [
                            "https://precioluzhoy-production-es.up.railway.app",
                              "https://precioluzhoy-es.vercel.app",
                             "http://localhost:3000",
                             "http://localhost:3001",
                             "http://localhost:3002",

                            
                            ]
                    )