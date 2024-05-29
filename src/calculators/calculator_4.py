from typing import List, Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler



class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler


    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        median = self.__calculate_median(input_data)
        response = self.__format_response(median)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado")
        
        input_data = body["numbers"]
        return input_data

    def __calculate_median(self, numbers: List[float]) -> float:
        median = self.__driver_handler.median(numbers)
        return median

    def __format_response(self, median:float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "Median": median,
                "sucess": True
            }
        }



