import os
from enum import Enum

from selenium import webdriver

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE_PATH = os.path.join(BASE_PATH, 'selenium/configuration')


class Driver(Enum):
    CHROME = 'Chrome'
    FIREFOX = 'Firefox'


driver_options = {
    Driver.CHROME: webdriver.ChromeOptions(),
    Driver.FIREFOX: webdriver.FirefoxOptions()
}
