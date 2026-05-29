from fixtures.excel_reader import get_test_data
from pages.login_page import LoginPage

def test_login(driver):
    data = get_test_data()

    login = LoginPage(driver)
    login.login(data["username"], data["password"])

    assert "inventory" in driver.current_url