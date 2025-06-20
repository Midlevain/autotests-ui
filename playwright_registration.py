from playwright.sync_api import  sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registration_page_registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_page_registration_button.click()

    dashboard_drawer = page.get_by_test_id("dashboard-drawer-list-item-button")
    expect(dashboard_drawer).to_be_visible()
    expect(dashboard_drawer).to_have_text('Dashboard')

    page.wait_for_timeout(5000)




#Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
#
#Заполнит поле "Email" значением "user.name@gmail.com" :rh:
#Заполнит поле "Username" значением "username" :ri:
#Заполнит поле "Password" значением "password" :rj:
#
#Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
#
#Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"
#
#data-testid="dashboard-drawer-list-item-button"
#python -m playwright_registration