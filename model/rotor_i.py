from interface.rotor import Rotor

class Rotor_I(Rotor):
    @property
    def name(self) -> str:
        return self._name

    @property
    def ring(self) -> list[str]:
        return self._ring

    @property
    def notch(self) -> str:
        return self._notch

    @property
    def turnover(self) -> str:
        return self._turnover

    @property
    def starting_position(self) -> int:
        return self._starting_position

    @property
    def actual_position(self) -> int:
        return self._actual_position
    
    def __init__(self, starting_position: int):
        self._name = 'I'
        self._ring = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
        self._notch = 'Y'
        self._turnover = 'Q'
        self._starting_position = starting_position

    @actual_position.setter
    def actual_position(self, actual_position: int):
        self._actual_position = actual_position
