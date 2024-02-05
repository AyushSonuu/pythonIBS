class Integer(int):

    def __init__(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.value = value

    def intValue(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            return False
        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            return True
        return self.value != other.value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            raise TypeError("Cannot compare with a non-Integer object")
        return self.value < other.value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            raise TypeError("Cannot compare with a non-Integer object")
        return self.value <= other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            raise TypeError("Cannot compare with a non-Integer object")
        return self.value > other.value

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            raise TypeError("Cannot compare with a non-Integer object")
        return self.value >= other.value

    def __repr__(self) -> str:
        return f"Integer({self.value})"

class Float(float):

    def __init__(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("value must be an ")
        self.value = value

    def floatValue(self) -> float:
        return self.value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Float ):
            return False
        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        if not isinstance(other,Float ):
            return True
        return self.value != other.value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Float):
            raise TypeError("Cannot compare with a non- object")
        return self.value < other.value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Float):
            raise TypeError("Cannot compare with a non- object")
        return self.value <= other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Float):
            raise TypeError("Cannot compare with a non- object")
        return self.value > other.value

    def __ge__(self, other: object) -> bool:
        if not isinstance(other,Float ):
            raise TypeError("Cannot compare with a non- object")
        return self.value >= other.value

    def __repr__(self) -> str:
        return f"({self.value})"

