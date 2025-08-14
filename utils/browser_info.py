def log_browser_info(driver):
    """
    Logs browser information including user-agent.
    """
    user_agent = driver.execute_script("return navigator.userAgent;")
    browser_name = driver.execute_script("return navigator.appName;")
    browser_version = driver.execute_script("return navigator.appVersion;")
    
    print(f"User-Agent: {user_agent}")
    print(f"Browser Name: {browser_name}")
    print(f"Browser Version: {browser_version}")
    
    return {
        "user_agent": user_agent,
        "browser_name": browser_name,
        "browser_version": browser_version
    }