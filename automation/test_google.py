from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    box = driver.find_element(By.NAME, "q")
    box.send_keys("pytest documentation" + Keys.RETURN)
    assert "pytest" in driver.title.lower()
    driver.quit()