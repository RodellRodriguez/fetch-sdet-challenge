from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


def run_test():
    # Get the absolute path to the chromedriver file, which is in the same directory as this python file.
    driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
    
    # Initialize the ChromeDriver service
    service = Service(executable_path=driver_path)
    
    # Initialize WebDriver with the service to set the chromedriver directory path
    driver = webdriver.Chrome(service=service)
    
    driver.get("http://sdetchallenge.fetch.com/")
    # Perform your automated actions here
    print(driver.title)
    from pdb import set_trace as bp
    bp()
    driver.quit()

'''
To- Do:

Implement the main algorithm
    Step 1: Divide the 9 bars into three groups of 3 bars each.
    Step 2: Weigh the first group against the second group using the balance scale.
        Case A: If the scale balances (both groups weigh the same), then the fake bar is in the third group that was not weighed.
        Case B: If the scale does not balance, the lighter group contains the fake bar.
    Step 3: Take the 3 bars from the group that contains the fake bar and repeat the process:
    Step 4: Divide these 3 bars into three groups of 1 bar each.
    Step 5: Weigh any two bars against each other.
        Case A: If the scale balances, the remaining unweighed bar is the fake one.
        Case B: If the scale does not balance, the lighter bar is the fake one.

Implement html web locators into the algorithm to read the weigh results to decide each decision tree
'''

if __name__ == "__main__":
    run_test()
