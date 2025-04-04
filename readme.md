# Browser Automation Project

## Overview
This project is designed for browser automation testing using **pytest**. It includes test scripts for login and survey functionalities.

This project utilizes [browser-use](https://github.com/browser-use/browser-use) for automation.

## Project Structure
```
browser_automation_project/
│── __pycache__/
│── tests/
│   ├── test_login.py
│   ├── test_survey.py
│── conftest.py
│── reports/
│── run_tests.sh
│── requirements.txt
│── pytest.ini
│── venv/
```

### Key Files:
- **tests/**: Contains test scripts.
  - `test_login.py`: Tests login functionality.
  - `test_survey.py`: Tests survey feature.
- **conftest.py**: Configuration file for pytest fixtures.
- **reports/**: Stores test execution reports.
- **run_tests.sh**: Script to run tests.
- **requirements.txt**: Lists dependencies.
- **pytest.ini**: Pytest configuration file.
- **venv/**: Virtual environment folder.

## Setup Instructions

### Prerequisites
Ensure you have **Python 3.8+** installed.

### Installation

#### For macOS/Linux
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd browser_automation_project
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

#### For Windows
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd browser_automation_project
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```sh
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests
Run all tests using:
```sh
pytest
```
Run a specific test:
```sh
pytest tests/test_login.py
```

Generate an HTML report:
```sh
pytest --html=reports/report.html
```

## Contributing
- Fork the repository.
- Create a new branch.
- Make your changes and submit a pull request.

## License
This project is licensed under the MIT License.

