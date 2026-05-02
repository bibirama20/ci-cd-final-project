from flask import Flask, jsonify
from service.models import db, Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
db.init_app(app)

@app.route("/")
def home():
    return jsonify({"message": "API Running"})