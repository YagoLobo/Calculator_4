from typing import List
from abc import ABC, abstractmethod

class DriverHandlerInterface(ABC):

    @abstractmethod
    def median(self, numbers: List[float]) -> float:
        pass