import pytest
from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()


def test_youtube():
    driver = webdriver.Edge()
    driver.get("https://www.youtube.com")
    assert "YouTube" in driver.title
    driver.quit()
