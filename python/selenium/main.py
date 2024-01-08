import pytest

from seleniumwire import webdriver
from configuration.config import load_selenium_config
from constants import CONFIG_FILE_PATH, Driver
import tests.test_flow_careers as careers
import tests.test_flow_login as login


# TODO: Enable Edge with a workaround for seleniumwire.
driver_options = {
    Driver.FIREFOX: 'selenium.webdriver.firefox.options.Options',
    Driver.CHROME: 'selenium.webdriver.chrome.options.Options',
    # Driver.EDGE: 'selenium.webdriver.edge.options.Options'
}


@pytest.fixture(scope="class")
def driver_init(request):
    config_file = request.config.getoption("--config")
    config_file = config_file or 'config.json'
    config = load_selenium_config(f"{CONFIG_FILE_PATH}/{config_file}")
    print(config.driver_name)

    seleniumwire_options = {'verify_ssl': False}

    driver_class = None
    options = None

    if config.driver_name.lower() == "firefox":
        from selenium.webdriver.firefox.options import Options
        driver_class = webdriver.Firefox
        options = Options()
    elif config.driver_name.lower() == "chrome":
        from selenium.webdriver.chrome.options import Options
        driver_class = webdriver.Chrome
        options = Options()
    # elif config.driver_name.lower() == "edge":
    #     from selenium.webdriver.edge.options import Options
    #     driver_class = webdriver.Edge
    #     options = Options()

    if config.driver_headless and options:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-oopr-debug-crash-dump")
        options.add_argument("--no-crash-upload")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-low-res-tiling")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")

    driver = driver_class(
        options=options,
        seleniumwire_options=seleniumwire_options
    )

    driver.set_window_size(config.driver_width, config.driver_height)
    driver.get(config.base_url)
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.config = config

    yield driver, config

    driver.quit()


@pytest.mark.usefixtures("driver_init")
class TestSelenium:

    def test_careers_button(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        careers.test_careers_button(driver, config)

    def test_open_positions_button(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        careers.test_open_positions_button(driver, config)

    def test_careers_job_positions(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        careers.test_careers_job_positions(driver, config)

    def test_careers_sections(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        careers.test_careers_sections(driver, config)

    def test_careers_filters(self):
        print(self.config.base_url)
        driver, config = self.driver, self.config
        careers.test_careers_filters(driver, config)

    def test_newsletter_subscription(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        careers.test_newsletter_subscription(driver, config)

    def test_login_valid(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_login_valid(driver, config)

    def test_valid_email_invalid_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_valid_email_invalid_password(driver, config)

    def test_invalid_email_valid_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_invalid_email_valid_password(driver, config)

    def test_invalid_email_invalid_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_invalid_email_invalid_password(driver, config)

    def test_unregistered_email_valid_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_unregistered_email_valid_password(driver, config)

    def test_registered_email_invalid_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_registered_email_invalid_password(driver, config)

    def test_valid_email_empty_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_valid_email_empty_password(driver, config)

    def test_empty_email_valid_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_empty_email_valid_password(driver, config)

    def test_empty_email_and_password(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_empty_email_and_password(driver, config)

    def test_forgot_password_valid_email(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_forgot_password_valid_email(driver, config)

    def test_forgot_password_invalid_email(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_forgot_password_invalid_email(driver, config)

    def test_forgot_password_without_email(self):
        print(self.config.driver_name)
        driver, config = self.driver, self.config
        login.test_forgot_password_without_email(driver, config)
