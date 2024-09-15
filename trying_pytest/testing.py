import pytest
from my_func import func, shapes
import time


def test_passing():
    pass


def test_pass():
    assert func.add(1, 2) == 3


# def test_fail():
#     assert func.add(1, 2) == 4


def zero_division():
    with pytest.raises(ZeroDivisionError):
        func.divide(1, 0)


def test_add_strings():
    result = func.add("hello", "world")
    assert result == "helloworld"


class TestCircle:
    def setup_method(self, method):
        print("setup_method")
        self.c = shapes.Circle(10)

    def teardown_method(self, method):
        print("teardown_method")
        del self.c

    def test_radius(self):
        assert self.c.radius == 10

    def perimeter(self):
        assert self.c.perimeter() == 2 * 3.14159 * 10

    def test_not_same(self, my_rectangle3):
        assert self.c.area() != my_rectangle3.area()


class TestRectangle:
    @pytest.fixture
    def my_rectangle(self):
        return shapes.Rectangle(10, 20)

    @pytest.fixture
    def my_rectangle2(self):
        return shapes.Rectangle(5, 6)

    def test_area(self, my_rectangle):
        assert my_rectangle.area() == 200

    def test_perimeter(self, my_rectangle):
        assert my_rectangle .perimeter() == 60

    def test_rect(self, my_rectangle, my_rectangle2):
        assert my_rectangle != my_rectangle2
        assert my_rectangle == shapes.Rectangle(10, 20)


@pytest.mark.slow
def test_slow():
    time.sleep(5)
    result = func.add(1, 2)
    assert result == 3


@pytest.mark.skip(reason="This test is currently broken ")
def skip_test():
    assert func.add(1, 2) == 3


@pytest.mark.xfail(reason="This test is impossible. ")
def test_impossible():
    func.divide(3, 0) # no assertions here


# Parameterized test
@pytest.mark.parametrize("side_length, expected_area", [(10, 100), (20, 400), (30, 900)]) # testing all these values
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area

