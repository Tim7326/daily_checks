from selenium import webdriver
from datetime import date, datetime
from webdriver_manager.chrome import ChromeDriverManager
import time
class spaceXBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.spacex.com/internships/")
        time.sleep(1)
        
    def get_internship(self):
        try:
            self.driver.find_element_by_xpath("//div[contains(text(), 'View Internships')]")\
                .click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//span[contains(text(), 'There are no jobs in this department.')]")
                internship = False   
            except: 
                internship = True
                print(internship)
        except: 
            print("Error!")    
        self.available = internship
        
    


check_internships = spaceXBot()
check_internships.get_internship()
print(check_internships.available)
print(check_internships)