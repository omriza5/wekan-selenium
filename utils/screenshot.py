import os

os.makedirs("artifacts/screenshots", exist_ok=True)

def take_screenshot(driver, name):
    """Helper function to take a screenshot."""
    driver.save_screenshot(f"artifacts/screenshots/{name}.png")
