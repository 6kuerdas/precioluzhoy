from typing import List, Optional, Dict
import datetime
import sqlmodel
from sqlmodel import Field
import sqlalchemy 
import reflex as rx
from sqlalchemy.dialects.postgresql import JSONB

class DatePrices(rx.Model, table=True):
    date: str
    # Add other fields here
    prices: List[float] = sqlmodel.Field(
        sa_column=sqlalchemy.Column(
            "prices",
            sqlalchemy.JSON  # or ARRAY(sqlalchemy.Float) depending on your database
        )
    )
    colors: List[str] = sqlmodel.Field(
        sa_column=sqlalchemy.Column(
            "colors", 
            sqlalchemy.JSON  # or ARRAY(sqlalchemy.String) depending on your database
        )
    )