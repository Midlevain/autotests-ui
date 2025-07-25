from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):

    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_toolbar = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_list_toolbar).to_be_visible()

    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    courses_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_view_title).to_be_visible()
    expect(courses_view_title).to_have_text('There is no results')

    courses_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_view_description).to_be_visible()
    expect(courses_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    #python -m pytest -s -v -k "test_empty_courses_list"