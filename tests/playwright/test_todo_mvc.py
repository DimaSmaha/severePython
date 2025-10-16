# pytest tests/playwright --headed
from playwright.sync_api import Page, expect

from config import Config


def test_has_title(page: Page):
    page.goto(Config.BASE_URL)
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill(
        "Go Shopping")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_have_text('Go Shopping')


class TestAbTestingPage(BaseTest):
    def setup_ab_testing_page(self):
        """Setup specific to AB Testing page tests."""
        self.page.goto(f"{self.base_url}/abtest")
        self.wait_for_page_load()
        self.ab_testing_page = AbTestingPage(self.page)
