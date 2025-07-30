from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Make the window full screen
    driver.get("https://duckduckgo.com")
    box = driver.find_element(By.NAME, "q")
    box.send_keys("pytest documentation" + Keys.RETURN)
    # Wait for the title to contain "pytest"
    WebDriverWait(driver, 10).until(EC.title_contains("pytest"))
    assert "pytest" in driver.title.lower()
    driver.quit()