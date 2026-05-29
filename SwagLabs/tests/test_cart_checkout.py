from fixtures.excel_reader import get_test_data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_full_flow(driver):

    data = get_test_data()

    login = LoginPage(driver)
    login.login(data["username"], data["password"])

    inventory = InventoryPage(driver)
    inventory.add_product()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details(
        data["first_name"],
        data["last_name"],
        data["zip_code"]
    )

    checkout.finish_order()
    success = checkout.get_success_text()

    assert "Thank you" in success