import config

db = config.db


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)
    image = db.Column(db.String(200))

    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image
