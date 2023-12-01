from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from utils.config import Config

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    return app

app = create_app()

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

@app.route("/", methods = ["GET"])
def greetings():
    return 'Hello World'

@app.route("/test-db", methods = ["GET"])
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return "Successfully connected to MY SQL-DB"
    except Exception as e:
        return f"Error in connecting to DB, Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug = True)