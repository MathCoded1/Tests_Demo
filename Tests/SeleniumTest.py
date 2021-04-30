import pytest
from Navigation import Navigation
from Tests import conftest


def test_LoginPageTitle(setUp):
    nav = Navigation.Navigate()
    assert nav.driver.title == 'Sign in to GitHub \xb7 GitHub'







