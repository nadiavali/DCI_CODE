class FizzBuzz:
    def __init__(self, integer):
        self.integer = integer

    def fizz(self):
        if self.integer % 3 == 0:
            return "Fizz"
        else:
            return self.integer

    def buzz(self):
        if self.integer % 5 == 0:
            return "Buzz"
        else:
            self.integer
    def fizz_buzz(self):
        if self.integer % 3 == 0 and self.integer % 5 == 0:
            return "FizzBuzz"
        else:
            return self.integer


