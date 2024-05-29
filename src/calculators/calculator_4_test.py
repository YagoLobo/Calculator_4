from src.calculators.calculator_4 import Calculator4
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    numpy_handler = NumpyHandler()
    mock_request = MockRequest({"numbers": [34 , 25]})
    calculator_4 = Calculator4(numpy_handler)
    
    response = calculator_4.calculate(mock_request)

    assert 'data' in response
    assert "Calculator" in response['data']
    assert "sucess" in response['data']
    print()
    print(response)
