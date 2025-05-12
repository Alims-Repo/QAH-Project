# E-Commerce Web Testing Framework

An automated testing framework built with Python and Selenium for testing e-commerce web applications.

## Project Structure

```
.
├── __init__.py
├── logs/
│   └── test_log.log
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── search_page.py
│   └── wishlist_page.py
├── pytest.ini
├── reports/
│   └── report.html
├── scripts/
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── regression/
│   │   ├── __init__.py
│   │   ├── test_add_to_cart.py
│   │   ├── test_search.py
│   │   └── test_wishlist.py
│   └── smoke/
│       ├── __init__.py
│       ├── test_login.py
│       ├── test_registration.py
│       └── test_search.py
├── test_data/
│   ├── MOCK_DATA.txt
│   └── Products_data.csv
└── utils/
    ├── __init__.py
    ├── config.py
    ├── csv_reader.py
    ├── data_scraper.py
    ├── database_reader.py
    ├── driver_factory.py
    └── json_reader.py
```

## Features

- **Page Object Model (POM)** design pattern for maintainable test code
- Separation of test data from test logic
- Multiple browser support through driver factory
- Support for different test types (smoke, regression)
- Data-driven testing using CSV files
- Comprehensive logging configuration
- HTML test reports generation
- Automatic screenshot capture for failed tests
- Database connectivity for advanced test scenarios

## Prerequisites

- Python 3.6+
- Selenium WebDriver
- Compatible web browsers (Chrome, Firefox)
- Corresponding WebDriver executables (chromedriver, geckodriver)
- MySQL Connector (for database tests)
- PyTest and plugins:
  - pytest-html (for HTML reports)
  - pytest-xdist (for parallel test execution)
  - pytest-selenium (for Selenium integration)
  - pytest-dependency (for test dependencies)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd e-commerce-test-framework
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Test Settings
Configure test settings in `utils/config.py`:

- BASE_URL: The main URL of the application being tested
- Browser selection and other environment-specific settings

### PyTest Configuration
The framework uses a `pytest.ini` file with the following configuration:

```ini
[pytest]
addopts = --html=reports/report.html --screenshot=on --screenshot_path=on -v -n 1
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)s] %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S
log_file = logs/test_log.log
log_file_level = INFO
log_file_format = %(asctime)s [%(levelname)s] %(message)s
log_file_date_format = %Y-%m-%d %H:%M:%S
log_file_append = true
log_auto_indent = true
log_file_live = true
```

This configuration enables:
- HTML report generation
- Automatic screenshot capture on test failure
- Console and file logging
- Parallel test execution (with `-n 1` currently set for single process)

## Test Data

Test data is stored in the `test_data` directory:

- `MOCK_DATA.txt`: User data for login and registration tests (CSV with semicolon delimiter)
  - Format: `first_name;last_name;email;telephone;password;newsletter`

- `Products_data.csv`: Product names for search tests (CSV with semicolon delimiter)
  - Format: `products`

### Database Configuration

For database-dependent tests, create a `db_creds.json` file with database credentials:

```json
{
  "host": "your_host",
  "user": "your_username",
  "password": "your_password",
  "database": "your_database"
}
```

## Running Tests

### Run all tests:

```bash
pytest
```

### Run specific test types:

```bash
pytest tests/smoke  # Run smoke tests
pytest tests/regression  # Run regression tests
```

### Run specific test file:

```bash
pytest tests/smoke/test_login.py
```

### Run with verbose output:

```bash
pytest -v tests/smoke/test_login.py
```

### Run tests in parallel:

```bash
pytest -n 4  # Run with 4 parallel processes
```

### Generate HTML report:

The HTML report is automatically generated in the `reports` directory when running tests. To view the latest report, open `reports/report.html` in a web browser after test execution.

## Logging

The framework uses Python's built-in logging module with both console and file logging:

- Console logs: Displayed during test execution with INFO level
- File logs: Saved to `logs/test_log.log` with INFO level

Example log entry:
```
2025-05-12 23:03:56 [INFO] Integration testcase to login then go to search page then search a product and add to cart being executed
```

To add logging to your tests or page objects:

```python
import logging

logger = logging.getLogger(__name__)
logger.info('Your log message here')
```

## Test Categories

### Smoke Tests

Basic functionality verification to ensure critical paths are working. Located in `tests/smoke/`:

- Login functionality
- User registration
- Product search

### Regression Tests

More comprehensive tests to ensure existing features work correctly. Located in `tests/regression/`:

- Add to cart functionality
- Search with multiple products
- Wishlist management

## Page Objects

The framework implements the Page Object Model pattern with the following pages:

### HomePage (`pages/home_page.py`)
- Handles interactions with the home page components
- Search functionality
- Product listing

### LoginPage (`pages/login_page.py`)
- Encapsulates login form operations
- Authentication

### RegistrationPage (`pages/registration_page.py`)
- Handles user registration process
- Form validation

### SearchPage (`pages/search_page.py`)
- Advanced search functionality
- Result validation
- Add to cart from search results

### WishlistPage (`pages/wishlist_page.py`)
- Wishlist management
- Product operations within wishlist

## Utilities

### config.py
- Configuration settings and URLs for different environments

### csv_reader.py
- Reading test data from CSV files with semicolon delimiter
- Skips header row automatically

### data_scraper.py
- Extract data from web elements for test validation
- Utility for scraping product information

### database_reader.py
- Database operations for data-driven testing
- Supports MySQL connections with query execution
- Insert and select operations

### driver_factory.py
- WebDriver initialization with browser selection
- Supports Chrome and Firefox

### json_reader.py
- Reading JSON configuration files
- Used for database credential management

## Best Practices

1. **Page Object Model**: Always use Page Object Model for new test cases
   - Keep element locators within the page classes
   - Use descriptive method names for actions

2. **Data Management**:
   - Keep test data separate from test logic
   - Use CSV files for data-driven testing
   - Store sensitive information in separate configuration files

3. **Test Methodology**:
   - Run smoke tests before regression tests
   - Mark tests appropriately with pytest markers
   - Use test dependencies when necessary

4. **Wait Strategies**:
   - Use explicit waits instead of sleep statements
   - Implement proper wait conditions with WebDriverWait

5. **Naming Conventions**:
   - Test methods: `test_*`
   - Page classes: `*Page`
   - Locator variables: descriptive with element type suffix (e.g., `login_btn`)

6. **Fixtures and Setup**:
   - Use fixtures for setup and teardown operations
   - Keep fixture scope as narrow as possible

7. **Logging**:
   - Add logging statements at appropriate levels
   - Log entry and exit points of significant actions
   - Include relevant data in log messages

8. **Error Handling**:
   - Use try-except blocks for expected exceptions
   - Implement proper assertions with meaningful messages

## Logging

The framework uses Python's built-in logging module. Logs are output to the console by default.

## Reports

Test reports are automatically generated in HTML format and stored in the `reports` directory. The reports include:

- Test summary with pass/fail statistics
- Detailed test case results
- Test duration information
- Failure details with screenshots
- Environment information

To view the reports, open `reports/report.html` in any web browser after test execution.

## Troubleshooting

### Common Issues:

1. **WebDriver executable not found**:
   - Ensure WebDriver executable (chromedriver, geckodriver) is in your system PATH
   - Or specify its location using the appropriate options

2. **Element not found exceptions**:
   - Use explicit waits with appropriate conditions
   - Verify locator strategies (XPath, CSS, etc.)
   - Check if the page has fully loaded

3. **Test data issues**:
   - Verify CSV format and delimiter (semicolon)
   - Check file path relative to project root
   - Ensure data types match expected input

4. **Database connection issues**:
   - Verify credentials in db_creds.json
   - Check network connectivity to database server
   - Ensure required database tables exist

5. **Parallel execution issues**:
   - Check for test dependencies that might cause conflicts
   - Adjust the number of parallel processes (-n parameter)
   - Ensure tests are isolated and don't share state

## Scripts

The `scripts` directory is available for custom Python scripts that support the testing process, such as:

- Test data generation
- Environment setup
- Test result analysis
- CI/CD integration scripts

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure no regressions
4. Update documentation as needed
5. Submit a pull request with a clear description of changes

## License

This project is licensed under the MIT License.