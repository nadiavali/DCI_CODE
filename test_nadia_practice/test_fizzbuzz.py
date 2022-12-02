from unittest import TestCase
from fizzbuzz import FizzBuzz

class FizzBuzzTest(TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self) -> None:
        return super().tearDown()


    def test_fizz_buzz_return_one(self):

        fizz_buzz = FizzBuzz()
        assert '1'== fizz_buzz.filter(1)
