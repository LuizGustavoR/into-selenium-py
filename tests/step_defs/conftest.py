"""
This module contains shared fixture.
"""

import json
import pytest
import selenium.webdriver as webdriver
from pytest_bdd import given
from pages.search import DuckDuckGoSearchPage

# scope='session' makes
# this fixture run only one time before the entire test suite
@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Accept values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Firefox', 'Headless Chrome']
    assert config['type'] in ['local', 'remote']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    assert isinstance(config['url_remote'], str)
    assert len(config['url_remote']) > 0

    # Return config so it can be used
    return config

# This fixture will run once for each test case
@pytest.fixture
def browser(config):
 
    # Initialize the local WebDriver instance
    if config['type'] == 'local':

        if config['browser'] == 'Firefox':
            opts = webdriver.FirefoxOptions()
            opts.add_argument('--window-size=1920,1080')
            browser = webdriver.Firefox(options=opts)
        elif config['browser'] == 'Chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('--window-size=1920,1080')
            browser = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported in local mode')

    # Initialize the remote WebDriver instance
    elif config['type'] == 'remote':

        if config['browser'] == 'Headless Firefox':
            opts = webdriver.FirefoxOptions()
        elif config['browser'] == 'Headless Chrome':
            opts = webdriver.ChromeOptions()
        else:
            raise Exception(f'Browser "{config["browser"]}" is not supported in remote mode')

        opts.add_argument('--no-sandbox')
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        browser = webdriver.Remote(
            command_executor = config['url_remote'],
            options=opts
        )

    # Make its calls wait for elements to appear
    browser.implicitly_wait(config['implicit_wait'])
 
    # Return the WebDriver instance for the setup
    yield browser
 
    # Quit the WebDriver instance for the instance
    browser.quit()

# Shared given steps
@given('the DuckDuckGo home page is displayed', target_fixture="duckduckgo_home")
def duckduckgo_home(browser):
    DuckDuckGoSearchPage(browser).load()
    pass

# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')