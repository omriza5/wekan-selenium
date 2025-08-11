import os

os.makedirs("artifacts/screenshots", exist_ok=True)
HEADLESS_MODE = os.environ.get("HEADLESS", None)

def take_screenshot(driver, name):
    """Helper function to take a screenshot."""
    if HEADLESS_MODE:
        driver.save_screenshot(f"artifacts/screenshots/{name}.png")
