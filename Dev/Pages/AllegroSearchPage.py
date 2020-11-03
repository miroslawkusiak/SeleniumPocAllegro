SITE_URL = 'https://allegro.pl/listing?string=Iphone%2011&bmatch=baseline-product-cl-eyesa2-engag-dict45-ele-1-1-0717&order=pd'


class AllegroSearchPage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(SITE_URL)

    def sort_scroll(self):
        return self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div/select")

    def black_color_selection(self):
        return self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div/div[12]/fieldset/div/ul/li[1]/label")
