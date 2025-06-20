from playwright.sync_api import  sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("Password")

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(5000)


    # user.name@gmail.com Login Password "Wrong email or password"
    #//div[@data-testid="login-form-email-input"]//div//input -- XPath локатор для поля почты
    # //div[@data-testid="login-form-password-input"]//div//input -- XPath локатор для поля пароля
    # //div//button[@data-testid="login-page-login-button"] -- локатор для кнопки Login
