import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page import ScalePage


EQUAL = 'equal'
LESS_THAN = 'less than'
GREATER_THAN = 'greater than'


def set_up():
    # Get the absolute path to the chromedriver file, which is in the same directory as run.sh
    driver_path = os.path.join(os.getcwd(), 'chromedriver')
    
    # Initialize the ChromeDriver service
    service = Service(executable_path=driver_path)
    
    # Initialize WebDriver with the service to set the chromedriver directory path
    driver = webdriver.Chrome(service=service)
    
    driver.get("http://sdetchallenge.fetch.com/")

    return driver

def main():
    driver = set_up()
    scale_page = ScalePage(driver)

    # Perform your automated actions here
    print(driver.title)

    fake_bar = find_fake_bar(scale_page)
    print(f"The fake bar is {fake_bar}.")
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

def find_fake_bar(scale_page):
    '''
    Returns the number of the fake bar and clicks on the fake bar in the website
    '''
    bars = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Represents each gold bar number
    
    # Weigh 1st group of 3 bars against 2nd group of 3 bars
    group1 = bars[0:3]
    group2 = bars[3:6]
    group3 = bars[6:9]
    
    weight_result = weigh_groups(scale_page, group1, group2)
    fake_bar = None

    if weight_result == EQUAL:
        # The fake bar is in group3
        fake_bar = weigh_individual(scale_page, group3, 6)
    elif weight_result == LESS_THAN:
        # The fake bar is in group1
        fake_bar = weigh_individual(scale_page, group1, 0)
    elif weight_result == GREATER_THAN:
        # The fake bar is in group2
        fake_bar = weigh_individual(scale_page, group2, 3)

    # To-Do: click on correct fake_bar, confirm the 'Yay! You find it!' alert appears and sleep for 3 seconds to allow user to see the message
    return fake_bar

def weigh_groups(scale_page, group_a, group_b):
    '''
    Weighs two groups against each other by filling in the bowls with group_a and group_b
    and returning equal, less than, or greater than.

    Equal, less than, and greater than corresponds to: group_a == group_b, group_a < group_b, and group_a > group_b
    '''
    pass 


def weigh_individual(group, start_index):
    '''
    Weighs two individual bars within the same group against each other by filling in the bowls
    and returning equal, less than, or greater than.
    '''
    # Weigh individual bars
    if group[0] == group[1]:
        return start_index + 2  # The fake bar is at the index corresponding to group[2]
    elif group[0] < group[1]:
        return start_index  # The fake bar is at the index corresponding to group[0]
    else:
        return start_index + 1  # The fake bar is at the index corresponding to group[1]


if __name__ == "__main__":
    main()
