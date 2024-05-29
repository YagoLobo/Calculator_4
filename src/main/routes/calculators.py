from flask import Blueprint, jsonify, request

calc4_route_bp = Blueprint("calc4_route", __name__)


@calc4_route_bp.route("/calculator/4", method=["POST"])
def calculator_4():
    pass