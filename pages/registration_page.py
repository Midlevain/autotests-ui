from playwright.sync_api import Page, expect
from pages.base_pages import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_registration_form_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_registration_form_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_registration_form_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.reregistration_page_registration_button = page.get_by_test_id('registration-page-registration-button')
        self.reregistration_page_login_link = page.get_by_test_id('registration-page-login-link')
        # self.registration_page_user_already_exist_alert = page.get_by_test_id('registration-page-user-already-exists-alert')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_registration_form_input.fill(email)
        expect(self.email_registration_form_input).to_have_value(email)

        self.username_registration_form_input.fill(username)
        expect(self.username_registration_form_input).to_have_value(username)

        self.password_registration_form_input.fill(password)
        expect(self.password_registration_form_input).to_have_value(password)

    def click_registration_button(self):
        self.reregistration_page_registration_button.click()

    def click_login_link(self):
        self.reregistration_page_login_link.click()

    # def check_user_already_exist_alert(self):
    #     expect(self.registration_page_user_already_exist_alert).to_be_visible()
    #     expect(self.registration_page_user_already_exist_alert).to_have_text('User already exists')