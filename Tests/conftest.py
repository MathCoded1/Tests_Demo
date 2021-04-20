import pytest
from Navigation import Navigation


@pytest.fixture()
def setUp(self):
    self.Nav = Navigation.Navigation()

