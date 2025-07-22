import pytest
from playwright.sync_api import expect, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize (
        'email, username, password,',
    [
        ("user.name@gmail.com", "username", "password"),
    ]
)

def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()
        dashboard_page.get_by_test_id('dashboard-toolbar-title-text')

        # email_input = chromium_page.get_by_test_id("registration-form-email-input").locator('input')
        # email_input.fill('user.name@gmail.com')
        #
        # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        # username_input.fill('username')
        #
        # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        # password_input.fill("password")

        # registration_page_registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        # registration_page_registration_button.click()
        #
        # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        # expect(dashboard_title).to_be_visible()

    #     context.storage_state(path='browser-state.json')
    #
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state='browser-state.json')
    #     page = context.new_page()
    #
    #     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    #
    #     courses_list_tooldbar = page.get_by_test_id('courses-list-toolbar-title-text')
    #     expect(courses_list_tooldbar).to_be_visible()
    #
    #     courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    #     expect(courses_icon).to_be_visible()
    #
    #     courses_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
    #     expect(courses_view_title).to_be_visible()
    #     expect(courses_view_title).to_have_text('There is no results')
    #
    #     courses_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
    #     expect(courses_view_description).to_be_visible()
    #     expect(courses_view_description).to_have_text('Results from the load test pipeline will be displayed here')
