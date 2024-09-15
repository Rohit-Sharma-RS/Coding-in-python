# Now we can make global rectangle fixtures in
import pytest
from my_func import shapes


@pytest.fixture
def my_rectangle3():
    return shapes.Rectangle(10, 20)
