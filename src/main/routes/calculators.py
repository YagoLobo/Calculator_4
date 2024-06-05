from flask import Blueprint, jsonify, request
from src.calculators.calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from src.errors.error_controller import handle_errors

calc4_route_bp = Blueprint("calc4_route", __name__)


@calc4_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        numpy_handler = NumpyHandler()
        calc = Calculator4(numpy_handler)
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]