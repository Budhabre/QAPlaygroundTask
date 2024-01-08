from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException
)


# TODO: Convert all selectors to variables.


def test_careers_button(driver, config):
    driver.get(config.base_url)

    element = WebDriverWait(driver, config.wait_timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                config.selector_home_careers_page_href
            )
        )
    )

    element.click()

    WebDriverWait(driver, config.wait_timeout).until(
        EC.url_to_be(config.careers_url)
    )

    assert driver.current_url == config.careers_url, "Careers button does not lead to the careers page."  # noqa: E501


def test_open_positions_button(driver, config):
    driver.get(config.base_url)

    careers_button = WebDriverWait(driver, config.wait_timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                config.selector_home_careers_page_href
            )
        )
    )

    careers_button.click()

    open_positions_button = WebDriverWait(driver, config.wait_timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                config.selector_careers_section_positions
            )
        )
    )
    open_positions_button.click()

    WebDriverWait(driver, config.wait_timeout).until(
        EC.url_to_be(config.careers_url)
    )

    assert driver.current_url == config.careers_url, "Open Positions button does not lead to the careers page."  # noqa: E501


def test_careers_job_positions(driver, config):
    driver.get(config.careers_url)

    element = WebDriverWait(driver, config.wait_timeout).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='tm-wrapper']"))
    )

    job_positions = element.find_elements(
        By.CSS_SELECTOR,
        config.selector_careers_position_title
    )

    for position in job_positions:
        title = position.text

        try:
            learn_more_btn = position.find_element(
                By.CSS_SELECTOR,
                config.selector_careers_position_description
            )

            # TODO: Check if the pdf is downloadable.
            assert learn_more_btn.get_attribute("href").endswith(".pdf"), \
                f"Learn More button for '{title}' does not link to a PDF."

            contact_btn = position.find_element(
                By.CSS_SELECTOR,
                config.selector_careers_position_apply_button
            )
            assert contact_btn.get_attribute("href").endswith("/contact"), \
                f"Contact button for '{title}' does not lead to /contact."

        except NoSuchElementException as e:
            assert False, f"Missing button(s) for '{title}': {e}"


def test_careers_sections(driver, config):
    driver.get(config.careers_url)
    section_selectors = [
        config.selector_careers_section_features,
        config.selector_careers_section_utility,
        config.selector_careers_section_above,
        config.selector_careers_section_positions,
        config.selector_careers_section_newsletter
    ]
    for selector in section_selectors:
        try:
            section = driver.find_element(By.XPATH, selector)
            children = section.find_elements(By.XPATH, "./*")
            assert len(children) > 0, (
                f"Section with selector '{selector}' "
                f"does not contain any child elements."
            )

        except NoSuchElementException as e:
            assert False, f"Section with selector '{selector}' not found: {e}"


def test_careers_filters(driver, config):
    driver.get(config.careers_url)
    WebDriverWait(driver, config.wait_timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.jl-subnav > li"))
    )
    filters = driver.find_elements(By.CSS_SELECTOR, "ul.jl-subnav > li")
    if not filters:
        assert False, "No filters found on the careers page."

    for filter_element in filters:
        filter_element.click()
        try:
            WebDriverWait(driver, config.wait_timeout).until(
                lambda d: d.find_elements(By.CSS_SELECTOR, "div.tm-wrapper")
            )
            data_tag = filter_element.get_attribute("jl-filter-control")
            if data_tag and "data-tag" in data_tag:
                tag_name = data_tag.split("'")[1]
                job_positions_selector = (
                    f"div.tm-wrapper[data-tag~"
                    f"='{tag_name}']"
                )
                is_all_filter = False
            else:
                job_positions_selector = "div.tm-wrapper"
                is_all_filter = True
            job_positions = driver.find_elements(
                By.CSS_SELECTOR,
                job_positions_selector
            )

            assert job_positions, (
                f"No job positions found for filter: "
                f"{filter_element.text}"
            )

            if not is_all_filter:
                for position in job_positions:
                    assert tag_name in position.get_attribute("data-tag"), \
                        (
                            f"Job position '{position.text}'"
                            f" does not match filter '{filter_element.text}'"
                        )

        except TimeoutException:
            assert False, (
                f"Timeout while waiting for job positions"
                f" to load for filter '{filter_element.text}'"
            )
        except NoSuchElementException as e:
            assert False, (
                f"Error finding job positions "
                f"for filter '{filter_element.text}': {e}"
            )


def test_newsletter_subscription(driver, config):
    driver.get(config.careers_url)

    try:
        test_email(
            driver,
            config.input_valid_email,
            True,
            config
        )
        test_email(
            driver,
            config.input_invalid_email,
            False,
            config
        )
    except (
            NoSuchElementException,
            StaleElementReferenceException,
            TimeoutException
    ) as e:
        assert False, f"Error during testing: {e}"


def test_email(driver_init, email, is_valid, config):
    try:
        email_input = WebDriverWait(driver_init, config.wait_timeout).until(
            EC.presence_of_element_located((By.ID, "newsletterUserMail"))
        )
        submit_button = WebDriverWait(driver_init, config.wait_timeout).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "button.bfCustomSubmitButton"
            ))
        )
        email_input.clear()
        email_input.send_keys(email)
        submit_button.click()

        if is_valid:
            WebDriverWait(driver_init, config.wait_timeout).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "div.form-notification.visible"
                ))
            )
            success_message = driver_init.find_element(
                By.CSS_SELECTOR,
                "div.form-notification.visible"
            )
            assert "thank you" in success_message.text.lower(), \
                "No success message for valid email"
        else:
            WebDriverWait(driver_init, config.wait_timeout).until(
                EC.visibility_of_element_located((
                    By.ID,
                    "newsletterErrorMessage"
                ))
            )
            error_message = driver_init.find_element(
                By.ID,
                "newsletterErrorMessage"
            )
            assert "invalid" in error_message.text.lower(), \
                "No error message for invalid email"

    except (
            NoSuchElementException,
            StaleElementReferenceException,
            TimeoutException
    ):
        assert False, "Error while testing newsletter subscription"
