import os
import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self,driver_path="D:/Projects/python/selenium_drivers",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        self.options = webdriver.ChromeOptions()
        self.options.headless = False
        super(Booking,self).__init__()
        self.implicitly_wait(15)
    
    def __exit__(self, exc_type, exc, traceback):
        print("Exiting")
        if self.teardown:
            self.quit

    
    def get_home_page(self):
        return self.get(const.BASE_URL)
