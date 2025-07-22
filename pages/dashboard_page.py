from playwright.sync_api import Page, expect
from pages.base_pages import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_page = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(self.dashboard_page).to_be_visible()