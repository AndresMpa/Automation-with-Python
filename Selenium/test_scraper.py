# Libraries
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ecs

# Scraper options
from selenium.webdriver.firefox.options import Options

# Skipping navigator instance creation
options = Options()
options.headless = True

# Using a proxy
PROXY = "127.63.13.19:3184"
options.add_argument('--proxy-server=%s' % PROXY)

# Scraper instance
path = './env/bin/geckodriver'
test_scraper = Firefox(executable_path=path, options=options)
