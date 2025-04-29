from math import gcd

class RationalValueError(ValueError):
    def __init__(self, message="Invalid operation with Rational numbers"):
        super().__init__(message)

class Rational:
    def __init__(self, numerator, denominator=None):
        if denominator is None:
            parts = numerator.split('/')
            numerator, denominator = int(parts[0]), int(parts[1])
        if denominator == 0:
            raise RationalValueError("Denominator cannot be zero")
        self.n = numerator
        self.d = denominator
        self.reduce()

    def reduce(self):
        common_divisor = gcd(self.n, self.d)
        self.n //= common_divisor
        self.d //= common_divisor

    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.d + other.n * self.d
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n + other * self.d
            return Rational(numerator, self.d)
        else:
            raise RationalValueError("Addition operation requires Rational or integer")

    def __sub__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.d - other.n * self.d
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n - other * self.d
            return Rational(numerator, self.d)
        else:
            raise RationalValueError("Subtraction operation requires Rational or integer")

    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.n
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n * other
            return Rational(numerator, self.d)
        else:
            raise RationalValueError("Multiplication operation requires Rational or integer")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalValueError("Division by zero is not allowed")
            numerator = self.n * other.d
            denominator = self.d * other.n
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            if other == 0:
                raise RationalValueError("Division by zero is not allowed")
            denominator = self.d * other
            return Rational(self.n, denominator)
        else:
            raise RationalValueError("Division operation requires Rational or integer")

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise RationalValueError("Invalid key for Rational")

    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise RationalValueError("Denominator cannot be zero")
            self.d = value
        else:
            raise RationalValueError("Invalid key for Rational")
        self.reduce()

    def __str__(self):
        return f"{self.n}/{self.d}"