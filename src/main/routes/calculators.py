from flask import Blueprint, jsonify, request
from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

calc4_route_bp = Blueprint("calc4_route", __name__)


@calc4_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    numpy_handler = NumpyHandler()
    calc = Calculator4(numpy_handler)
    response = calc.calculate(request)

    return jsonify(response), 200