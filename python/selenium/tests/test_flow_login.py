import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


# TODO: Move inputs to variables.


def test_login_valid(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field
    )
    email_field.click()
    email_field.send_keys(config.input_valid_email)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(config.input_valid_password)
    password_field.send_keys(Keys.ENTER)

    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            # NOTE: We don't have a valid credential but if we did we can
            # use: EC.presence_of_element_located((By.XPATH,
            # '//*[@id="your-success-login-element-xpath"]'))
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_email_field
            ))
        )
        assert element, "Login failed: Success element not found after login"
        print("Pass the test! Element found after login.")

        # TODO: We can add a check for the landing URL after login if we had
        #  credentials. assert driver.current_url ==
        #  "https://www.domain.com", "Unexpected landing URL after login"

        # TODO: We can find an element after a successful login. assert
        #  "Welcome" in driver.page_source, "Login success message not found"

    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"


def test_valid_email_invalid_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)

    email_field = driver.find_element(By.XPATH, config.selector_email_field)
    email_field.click()
    email_field.send_keys(config.input_valid_email)

    password_field = driver.find_element(By.XPATH, config.selector_password_field)
    password_field.click()
    password_field.send_keys(config.input_invalid_password)

    password_field.send_keys(Keys.ENTER)

    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.visibility_of_element_located((By.XPATH, config.selector_login_notification))
        )

        assert element is not None
        print("Pass the test! Element found after login.")

    except TimeoutException:
        print("Error: Element not found or not visible on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"

    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_invalid_email_valid_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field
    )
    email_field.click()
    email_field.send_keys(config.input_invalid_email)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(config.input_valid_password)
    password_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_invalid_email_invalid_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field
    )
    email_field.click()
    email_field.send_keys(config.input_invalid_email)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(config.input_invalid_password)
    password_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_unregistered_email_valid_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field
    )
    email_field.click()
    email_field.send_keys(config.input_unregistered_email)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(config.input_valid_password)
    password_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_registered_email_invalid_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field
    )
    email_field.click()
    email_field.send_keys(config.input_registered_email)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(config.input_invalid_password)
    password_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_valid_email_empty_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field
    )
    email_field.click()
    email_field.send_keys(config.input_valid_email)
    email_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_empty_email_valid_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(config.input_invalid_password)
    password_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_empty_email_and_password(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    password_field = driver.find_element(
        By.XPATH,
        config.selector_password_field
    )
    password_field.click()
    password_field.send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                config.selector_login_notification
            ))
        )
        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_forgot_password_valid_email(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)

    forgot_your_password = driver.find_element(By.XPATH, config.selector_login_forgot_password_link)
    forgot_your_password.click()
    time.sleep(config.wait_timeout)

    email_field = driver.find_element(By.XPATH, config.selector_email_field_forgot_password)
    email_field.send_keys(config.input_valid_email)
    email_field.send_keys(Keys.ENTER)

    try:
        element = WebDriverWait(driver, config.wait_timeout).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{config.selector_expected_text_in_password_confirmation}')]"))
        )

        assert element is not None
        print("Pass the test! Element found after login.")
    except TimeoutException:
        print("Error: Element not found or does not contain the expected text.")
        assert False, "Login failed: Timeout while waiting for success element"

    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_forgot_password_invalid_email(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    forgot_your_password = driver.find_element(
        By.XPATH,
        config.selector_login_forgot_password_link
    )
    forgot_your_password.click()
    time.sleep(config.wait_timeout)
    email_field = driver.find_element(
        By.XPATH,
        config.selector_email_field_forgot_password
    )
    email_field.send_keys(config.input_invalid_email)
    email_field.send_keys(Keys.ENTER)
    expected_url = "https://marketplace.mitigram.com/Account/ForgotPassword"
    try:
        assert driver.current_url == expected_url
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
        assert False, "Login failed: Timeout while waiting for success element"
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)


def test_forgot_password_without_email(driver, config):
    driver.get(config.base_url)
    log_in = WebDriverWait(driver, config.wait_timeout).until(
        EC.element_to_be_clickable((By.XPATH, config.selector_login_button))
    )
    log_in.click()
    time.sleep(config.wait_timeout)
    forgot_your_password = driver.find_element(
        By.XPATH,
        config.selector_login_forgot_password_link
    )
    forgot_your_password.click()
    time.sleep(config.wait_timeout)
    submit_button = driver.find_element(
        By.XPATH,
        '/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/form/div[2]/input'
    )
    submit_button.click()
    time.sleep(config.wait_timeout)
    expected_url = "https://marketplace.mitigram.com/Account/ForgotPassword"
    try:
        assert driver.current_url == expected_url
    except TimeoutException:
        print("Error: Element not found on the new page after login.")
    time.sleep(config.wait_timeout)
    driver.get(config.base_url)
