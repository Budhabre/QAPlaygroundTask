import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.common.keys import Keys


def test_page_performance(driver):
    wait = WebDriverWait(driver, config.wait_timeout)
    start_time = time.time()
    main_request_temp = config.base_url if config.base_url.endswith('/') else config.base_url + '/'
    main_request = next((req for req in driver.requests if req.response and req.url == main_request_temp), None)
    if main_request is None:
        self.fail("Main request not found")
    self.assertEqual(main_request.response.status_code, 200, "HTTP response code is not 200")
    total_size = sum(len(req.response.body) for req in driver.requests if req.response)
    total_size_mb = total_size / (1024 * 1024)
    self.assertTrue(total_size_mb < config.max_total_size, f"Total size is too large - {total_size_mb} MB")
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    self.assertTrue(elapsed_time < config.max_response_time, "Response time is too long")