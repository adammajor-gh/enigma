from abc import ABC, abstractmethod

class Rotor(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def ring(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def notch(self) -> str:
        pass

    @property
    @abstractmethod
    def turnover(self) -> str:
        pass

    @property
    @abstractmethod
    def starting_position(self) -> int:
        pass

    @property
    def alphabet(self) -> str:
        return ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

    @abstractmethod
    def __init__(self, starting_position: int):
        pass

    def rotate_backward(self):
        last_char = self.ring.pop()
        self.ring.insert(0, last_char)

    def rotate_forward(self):
        first_char = self.ring.pop(0)
        self.ring.append(first_char)

    def get_encoded_letter(self, orig_letter:str) -> str:
        orig_letter = orig_letter.upper()
        orig_letter_index = self.alphabet.index(orig_letter)
        encoded_letter = self.ring[orig_letter_index]
        return encoded_letter