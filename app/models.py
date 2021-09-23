from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app
# Create database connection object
db = SQLAlchemy(app)

class Car(db.Model):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    maker = Column(String)
    model = Column(String)
    mileage = Column(Integer)
    manufacture_year = Column(String)
    engine_displacement = Column(String)
    engine_power = Column(String)
    color_slug = Column(String)
    transmission = Column(String)
    door_count = Column(Integer)
    seat_count = Column(Integer)
    fuel_type = Column(String)
    price_eur = Column(Float)

    def __init__(self, maker, model, mileage, manufacture_year, engine_displacement, engine_power, color_slug,
                 transmission, door_count, seat_count, fuel_type, price_eur):
        self.maker = maker
        self.model = model
        self.mileage = mileage
        self.manufacture_year = manufacture_year
        self.engine_displacement = engine_displacement
        self.engine_power = engine_power
        self.color_slug = color_slug
        self.transmission = transmission
        self.door_count = door_count
        self.seat_count = seat_count
        self.fuel_type = fuel_type
        self.price_eur = price_eur

    def format(self):
    return {
        'id': self.id,
        'maker': self.maker,
        'model': self.model,
        'mileage': self.mileage,
        'manufacture_year': self.manufacture_year,
        'engine_displacement': self.engine_displacement,
        'engine_power': self.engine_power,
        'color_slug ': self.color_slug,
        'transmission': self.transmission,
        'door_count': self.door_count,
        'seat_count': self.seat_count,
        'fuel_type': self.fuel_type,
        'price_eur': self.price_eur
    }