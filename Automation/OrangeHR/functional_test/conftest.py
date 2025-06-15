import pytest
import os

# Store plugin reference
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

    # Only try to set metadata if pytest-html plugin is enabled
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'OrangeHRM Login Automation'
        config._metadata['Tested By'] = 'Dylan'
        config._metadata['Environment'] = 'UAT'
        config._metadata['Browser'] = 'Chrome'

# Optional: Modify or clear metadata
def pytest_metadata(metadata):
    metadata["Project Name"] = 'OrangeHRM Login Automation'
    metadata["Tested By"] = "Dylan"
    metadata["Environment"] = "UAT"
    metadata["Browser"] = "Chrome"

# Add screenshots for failed tests
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            print(f"📸 Screenshot saved: {screenshot_path}")

            if screenshot_path:
                html = f'<div><img src="../{screenshot_path}" alt="screenshot" ' \
                       f'style="width:400px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

    report.extra = extra
