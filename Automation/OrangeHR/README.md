# OrangeHRM Login Automation

This project contains automated functional tests for the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/), focusing on the login module. The tests are written using **Selenium WebDriver** with **Python** and executed using **pytest**.

---

## Folder Structure

```plaintext
orangehrm-automation/
├── functional_test/
│   ├── __init__.py
│   ├── conftest.py              # Pytest hooks (e.g., screenshot, metadata)
│   ├── test_login.py            # Main test script
│   └── testdata/
│       └── test_login_data.xlsx # Excel data for data-driven tests
│
├── screenshots/                 # Screenshots saved on test failure
├── report.html                  # Generated HTML report

cmd:
pytest functional_test/test_login.py -v --html=reports/test_report.html --self-contained-html
