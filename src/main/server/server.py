from flask import Flask
from src.main.routes.calculators import calc4_route_bp

app = Flask(__name__)

app.register_blueprint(calc4_route_bp)