# AutoQAPlayground

## Pre-requisites
1. Python 3.10+
2. Virtualenv

## Setup
1. Create a virtualenv: `virtualenv venv`
2. Activate the virtualenv: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the tests: `pytest python_module/selenium_module/main.py`
- To use a specific `config file`: `pytest python_module/selenium_module/main.py --config {file_name}.json`
- NOTE: The `config file` must be in the configurations folder. The default config file is `sample_config.json`.

## Requirements

1. Use nice loggers instead of print statements.
2. All tests must be done with asserts unless they are already wrapped by the tool.
3. We must always have requirements.txt / package.json / etc. for each language.
4. All secrets must be gitignored (and example must be provided).
5. Add TODOs and NOTEs where needed (to show knowledge of best practices).
