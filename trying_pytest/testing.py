import pytest
from my_func import func, shapes


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

