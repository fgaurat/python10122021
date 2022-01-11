

class DivBy12Error(ArithmeticError):


    def __init__(self) -> None:
        super().__init__("Division par 12 !")
        print("DivBy12Error def __init__(self)")