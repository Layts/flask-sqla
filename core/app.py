from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from core.srv.config import DB_URL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import core.routers as router
app.register_blueprint(router.app_route)



