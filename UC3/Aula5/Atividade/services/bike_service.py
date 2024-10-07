from models.bike_model import Bike

class BikeService:
    def __init__(self):
        self.bikes = []

    def add_bike(self, model, category, price):
        if any(bike.model == model for bike in self.bikes):
            raise ValueError("Modelo de bicicleta já existe.")
        if price < 100:
            raise ValueError("O preço deve ser no mínimo R$ 100,00.")
        new_bike = Bike(model, category, price)
        self.bikes.append(new_bike)

    def get_all_bikes(self):
        return self.bikes

    def sell_bike(self, model):
        for bike in self.bikes:
            if bike.model == model:
                bike.status = 'Vendida'
                break

    def delete_bike(self, model):
        self.bikes = [bike for bike in self.bikes if bike.model != model]
