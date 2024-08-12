from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# Example Selenium script
def run_test():
    # Get the absolute path to the chromedriver
    driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
    
    # Initialize the ChromeDriver service
    service = Service(executable_path=driver_path)
    
    # Initialize WebDriver with the service
    driver = webdriver.Chrome(service=service)
    
    driver.get("http://sdetchallenge.fetch.com/")
    # Perform your automated actions here
    print(driver.title)
    from pdb import set_trace as bp
    bp()
    driver.quit()

if __name__ == "__main__":
    run_test()
