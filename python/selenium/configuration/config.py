import os
from typing import Type
from typing import Dict

from pydantic import BaseModel


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_PATH, '.env')


class SeleniumConfig(BaseModel):
    base_url: str = 'https://www.mitigram.com'
    careers_url: str = 'https://www.mitigram.com/careers'
    driver_name: str = 'Chrome'
    wait_timeout: int = 10
    max_response_time: int = 5000
    max_total_size: int = 10 * 1024 * 1024
    driver_headless: bool = False
    driver_width: int = 1920
    driver_height: int = 1080
    input_valid_email: str = 'valid-email@nodomain.com'
    input_invalid_email: str = 'invalid-email@@nodomain.com'
    input_registered_email: str = "registered-email@nodomain.com"
    input_unregistered_email: str = "unregistered-email@nodomain.com"
    input_valid_password: str = ''
    input_invalid_password: str = ''
    selector_home_login_page_button: str = '#custom-8397-particle > a.jl-button.jl-button-white-negative'
    selector_home_careers_page_href: str = '/html/body/div[3]/footer/div/div[2]/div[5]/div/a[3]'
    selector_email_field: str = '/html/body/div/div/div[2]/div/div[1]/form/div/div[2]/div/fieldset[1]/input'
    selector_password_field: str = '/html/body/div/div/div[2]/div/div[1]/form/div/div[2]/div/fieldset[2]/input'
    selector_expected_text_in_password_confirmation: str = "Forgot Password Confirmation"
    selector_email_field_forgot_password: str = "/html/body/div/div/div[2]/div/div/div/div/div/div[2]/div/form/fieldset/input"
    selector_login_button: str = '/html/body/div[3]/section[1]/div/div[2]/div[3]/div/a[2]'
    selector_login_notification: str = '/html/body/div/div/div[2]/div/div[1]/form/div/div[1]/div/div[1]'
    selector_login_forgot_password_link: str = '/html/body/div/div/div[2]/div/div[1]/form/div/div[2]/div/div[1]/div/a'
    selector_careers_section_features: str = '//*[@id="g-features"]'
    selector_careers_section_utility: str = '//*[@id="g-utility"]'
    selector_careers_section_above: str = '//*[@id="g-above"]'
    selector_careers_section_positions: str = '//*[@id="g-open-positions"]'
    selector_careers_section_newsletter: str = '//*[@id="g-newsletter"]'
    selector_careers_accordion: str = '.js-module-jlfaq-205'
    selector_careers_positions_wrapper: str = '.tm-wrapper'
    selector_careers_position_title: str = '.jl-title'
    selector_careers_position_description: str = 'a.jl-button-primary'
    selector_careers_position_apply_button: str = 'a.jl-button-black-negative'

    class Config:
        case_sensitive: bool = False
        env_prefix = "CFG_"


def load_settings_from_file(file_path: str, config_class: Type[SeleniumConfig]) -> SeleniumConfig:
    with open(file_path, 'r') as file:
        json_data = file.read()
    return config_class.model_validate_json(json_data)


def parse_env_data(env_data: str, prefix: str) -> Dict[str, str]:
    return {key[len(prefix):]: value for line in env_data.split('\n') if line.strip() and not line.startswith('#') for key, value in [line.strip().split('=', 1)] if key.startswith(prefix)}  # noqa: E501


def update_settings_from_file(settings: SeleniumConfig, file_path: str) -> None:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            env_data = file.read()
            env_settings = parse_env_data(env_data, SeleniumConfig.Config.env_prefix)
            updated_settings = settings.model_copy(update=env_settings)
            settings.__dict__.update(updated_settings.__dict__)


def update_settings_from_env(settings: SeleniumConfig) -> None:
    for field_name, field in settings.__annotations__.items():
        env_var_name = f"{SeleniumConfig.Config.env_prefix}{field_name.upper()}"
        if env_var_name in os.environ:
            setattr(settings, field_name, os.environ[env_var_name])


def load_selenium_config(json_file_path: str) -> SeleniumConfig:
    settings = load_settings_from_file(json_file_path, SeleniumConfig)
    update_settings_from_file(settings, ENV_PATH)
    update_settings_from_env(settings)
    return settings