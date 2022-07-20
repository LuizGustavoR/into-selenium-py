from pytest_bdd import scenarios, given, when, then, parsers

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

scenarios('../features/web.feature')

@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for {text}'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    DuckDuckGoSearchPage(browser).search(text)

@then(parsers.parse('results title contains "{phrase}"'))
def search_results_title(browser, phrase):
    assert WebDriverWait(browser, 5).until(EC.title_contains(phrase))

@then(parsers.parse('results are shown for {phrase}'))
def results_have_one(browser, phrase):
    results = DuckDuckGoResultPage(browser).result_link_titles()
    assert len(results) > 0
    assert DuckDuckGoResultPage(browser).search_input_value() == phrase

@then(parsers.parse('one of the results contains "{phrase}"'))
def search_results(browser, phrase):
    results = DuckDuckGoResultPage(browser).result_link_titles()
    assert any(phrase in s for s in results)
