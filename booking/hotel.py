from selenium.webdriver.remote.webelement import WebElement

class Report:
        def __init__(self,bse:WebElement):
            self.bse=bse
            self.deal_boxes=self.pull_deal_boxes()
                    
        def pull_deal_boxes(self):
            return self.bse.find_elements_by_css_selector(
                'div[data-testid="property-card"]'
            )
        
        def pull_titles(self):
            coll=[]
            print("in hotels")
            for deal_box in self.deal_boxes:
                hn=deal_box.find_element_by_css_selector(
                    'div[data-testid="title"]'
                ).get_attribute('innerHTML').strip()
                print (hn)
                
                # hpricediv=deal_box.find_element_by_css_selector(
                #     'div[data-testid="price-and-discounted-price"] '
                # )
                # hpdchildren=hpricediv.find_element_by_css_selector('*')
                # print(hpdchildren)
                # for i in hpdchildren:
                #     print (i.get_attribute('innerHTML').strip())
                # print (hprice)
                
                score=deal_box.get_attribute('aria-label')
                
                coll.append(
                    [hn,score]
                )
                return (coll)
                
                
                
            