from selenium.webdriver.remote.webdriver import WebDriver


class BookingFilters:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        
    def stars(self,*star):
        star_div=self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_children=star_div.find_elements_by_css_selector("*")
        
        for j in star:
            for i in star_children:
                if str(i.get_attribute("innerHTML")).strip()==f"{j} stars":
                    i.click()
                    
    def facility(self,whatfac):    
        fac_div=self.driver.find_element_by_css_selector(
                'div[data-filters-group="hotelfacility"]'
            )
        fac_children=fac_div.find_elements_by_css_selector("*")
        
        for i in fac_children:
                if str(i.get_attribute("innerHTML")).strip()==f"{whatfac}":
                    i.click()
                    
    def sortingg(self):
            tab=self.driver.find_element_by_css_selector(
                'li[data-id="upsort_bh"]'
            ).click()
    
            
    
        
        
        
    

    