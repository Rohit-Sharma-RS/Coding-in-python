import pytest
from my_func import func, shapes, service
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


# @pytest.mark.slow
# def test_slow():
#     time.sleep(5)
#     result = func.add(1, 2)
#     assert result == 3


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


# Mocking from service.py
import unittest.mock as mock


@mock.patch("my_func.service.database")
def test_get_user_from_db(mock_db): # name this anything does not matter
    mock_db.get.return_value = "Mocked Alice"
    assert service.get_user_from_db(1) == "Mocked Alice"


@mock.patch("requests.get")  # this says replace requests.get with mock_get 👇
def test_get_users(mock_get):
    mock_response = mock.Mock()  # this is what creates the fake entity of requests.get
    mock_response.status_code = 200  # fake the status code to be 200
    mock_response.json.return_value = "Mocked data"  # this is what we want to return
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == "Mocked data"


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == "Error fetching data"


# Now let us use chatgpt to test the school.py
# using pytest and functions that come from it such as fixtures, parameterize, raises and mock wherever necessary
# test the following code set the theme of harry potter.

from my_func.school import *
# Fixtures for reusable test objects
@pytest.fixture
def teacher_snape():
    return Teacher(name="Severus Snape", age=38)


@pytest.fixture
def teacher_mcgonagall():
    return Teacher(name="Minerva McGonagall", age=65)


@pytest.fixture
def student_harry():
    return Student(name="Harry Potter", age=17)


@pytest.fixture
def student_hermione():
    return Student(name="Hermione Granger", age=17)


@pytest.fixture
def student_ron():
    return Student(name="Ron Weasley", age=17)


@pytest.fixture
def classroom(teacher_snape, student_harry, student_hermione):
    # Initial classroom setup with 2 students
    return Classroom(teacher=teacher_snape, course_title="Defense Against the Dark Arts",
                     students=[student_harry, student_hermione])


# Test adding a student
def test_add_student(classroom, student_ron):
    classroom.add_student(student_ron)
    assert student_ron in classroom.students


# Test adding too many students
def test_add_too_many_students(classroom):
    # Fill up the classroom to the max (20 students)
    for i in range(18):
        classroom.add_student(Student(f"Student {i + 1}", 17))

    # Test that adding one more student raises an exception
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student(name="Neville Longbottom", age=17))


# Test removing a student
def test_remove_student(classroom):
    classroom.remove_student("Hermione Granger")
    assert not any(student.name == "Hermione Granger" for student in classroom.students)


# Test changing the teacher
def test_change_teacher(classroom, teacher_mcgonagall):
    classroom.change_teacher(teacher_mcgonagall)
    assert classroom.teacher.name == "Minerva McGonagall"


# Parameterized test to check multiple student additions
@pytest.mark.parametrize("student_name", [
    ("Draco Malfoy"),
    ("Luna Lovegood"),
    ("Neville Longbottom")
])
def test_add_multiple_students(classroom, student_name):
    student = Student(name=student_name, age=17)
    classroom.add_student(student)
    assert student in classroom.students


# Mocking example (not strictly necessary here, but to demonstrate)
def test_mock_change_teacher():
    classroom = mock.Mock()
    new_teacher = Teacher(name="Gilderoy Lockhart", age=33)

    classroom.change_teacher(new_teacher)
    classroom.change_teacher.assert_called_with(new_teacher)
