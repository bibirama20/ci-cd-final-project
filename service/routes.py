from flask import Flask, jsonify
from service.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
db.init_app(app)


@app.route("/")
def home():
    return jsonify({"message": "API Running"})

if __name__ == "__main__":
    print("SERVICERUNNING on port 8000")
    app.run(host="0.0.0.0", port=8000)
