# RealPha Web Test Suite

This project contains automated tests for the RealPha web application using Playwright and pytest.

## Prerequisites

- Python 3.12+
- pip (Python package manager)

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv myenv
```

### 2. Activate Virtual Environment

**On Linux/macOS:**
```bash
source myenv/bin/activate
```

**On Windows:**
```bash
myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

After installing dependencies, you need to install the browser binaries for Playwright:

```bash
playwright install chromium
```

Or to install all supported browsers:
```bash
playwright install
```

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

Run the calculate rebate tests:
```bash
pytest tests/test_calculate_rebate.py
```

Run the signup tests:
```bash
pytest tests/test_signup.py
```

Run the save search tests:
```bash
pytest tests/test_saveSearch.py
```

Run the RealPha realty mortgage flow tests:
```bash
pytest tests/test_realpha_realty_mortgage_flow.py
```

### Run Tests with Specific Options

**Run in headless mode (no browser window):**
```bash
pytest --headed=False
```

**Run with a different browser:**
```bash
pytest --browser firefox
pytest --browser webkit
```

**Run with custom slow motion (in milliseconds):**
```bash
pytest --slowmo=500
```

**Run with verbose output:**
```bash
pytest -v
```

**Run specific test function:**
```bash
pytest tests/test_signup.py::test_user_registration
```

## Configuration

The test configuration is defined in `pytest.ini`:

- **Default browser:** Chromium
- **Default mode:** Headed (browser window visible)
- **Slow motion:** 200ms (helps visualize automation)
- **Test path:** tests/

You can override these defaults using command-line options when running pytest.

## Project Structure

```
realphaweb/
├── pages/              # Page Object Models for different web pages
│   ├── login_page.py
│   ├── signup_page.py
│   └── unified_flow.py
├── tests/              # Test files
│   ├── test_calculate_rebate.py
│   ├── test_signup.py
│   ├── test_saveSearch.py
│   └── test_realpha_realty_mortgage_flow.py
├── utils/              # Utility functions
├── conftest.py         # Pytest configuration and fixtures
├── pytest.ini          # Pytest settings
└── requirements.txt    # Python dependencies
```

## Dependencies

- **pytest** - Test framework
- **pytest-playwright** - Pytest plugin for Playwright
- **pytest-base-url** - Base URL fixture for tests
- **playwright** - Browser automation library
- Other utilities for web testing and data manipulation

## Deactivating Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

### Playwright browsers not found
Run: `playwright install chromium`

### Permission denied when running tests
Make sure the virtual environment is properly activated and you have execute permissions

### Tests failing to find base URL
Check `conftest.py` for fixture configurations and ensure the application is running on the expected URL


