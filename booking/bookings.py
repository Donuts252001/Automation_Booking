from selenium import webdriver
import os
import booking.constant as const
from booking.bookingfilters import BookingFilters
from booking.hotel import Report
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Users/vaish/Desktop/Self Learning/Cloud/DEVOPS/SELENIUM",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] +=self.driver_path
        
        options=webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        super(Booking,self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()
        
    def land(self):
        self.get(const.BASE_URL)
    
    def __exit__(self, *args):
        if self.teardown:
                    self.quit()
                    
    
    def curr(self,currency=None):
        curr=self.find_element_by_css_selector(
            "button[data-tooltip-text='Choose your currency']"
        )
        curr.click()
        
        select_curr=self.find_element_by_css_selector(
            f"a[data-modal-header-async-url-param*='selected_currency={currency}']"
        )
        select_curr.click()
        
    def going(self,place):
        going_input=self.find_element_by_id("ss")
        going_input.clear()
        going_input.send_keys(place)
        
        select_place=self.find_element_by_css_selector(
            "li[data-i='0']"
        )
        select_place.click()
    
    def when(self,godate,comedate):
        select_go=self.find_element_by_css_selector(
            f"td[data-date='{godate}']"
        )
        select_go.click()
        
        select_come=self.find_element_by_css_selector(
            f"td[data-date='{comedate}']"
        )
        select_come.click()
        
    def who(self,count=0):
        open=self.find_element_by_id('xp__guests__toggle')
        open.click()
        
        val=self.find_element_by_id("group_adults")
        val_adults=val.get_attribute('value')
        adults=int(val_adults)
        
        while(adults!=1):
            minus=self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            minus.click()
            adults=adults-1
            
        while(adults!=count):
            add=self.find_element_by_css_selector(
                'button[aria-label="Increase number of Adults"]'
            ).click()
            adults=adults+1
            
    def search(self):
        searchb=self.find_element_by_css_selector(
            "button[type='submit']"
        )
        searchb.click()
        
    def apply_filters(self):
        print("filters applied")
        filters=BookingFilters(driver=self)
        filters.stars(3,4)
        filters.facility("Fitness center")
        # filters.sortingg()
        # filters.report_class()
    
    def report_class(self):
        print("reporting")
        hotelboxes=self.find_element_by_css_selector(
            'div[data-block-id="hotel_list"]'
        )
        repoi=Report(hotelboxes)
        print(repoi.pull_titles())
        # table=PrettyTable(
        #     field_deal_boxs=['Hotel deal_boxs','prices','scores']
        # )
        # table.add_rows(repoi.pull_titles())
        # print(table) 
        
        print("reporting done")       