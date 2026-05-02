from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))
    category = db.Column(db.String(63))
    available = db.Column(db.Boolean)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "available": self.available
        }
    