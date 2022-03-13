"""
This module contains shared fixture.
"""

import json
import pytest
import selenium.webdriver

# scope='session' makes
# this fixture run only one time before the entire test suite
@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Accept values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

# This fixture will run once for each test case
@pytest.fixture
def browser(config):
 
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        opts.add_argument('--log-level=1')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
 
    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])
 
    # Return the WebDriver instance for the setup
    yield b
 
    # Quit the WebDriver instance for the instance
    b.quit