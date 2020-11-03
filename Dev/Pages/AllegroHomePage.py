SITE_URL = 'https://allegro.pl'


class AllegroHomePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(SITE_URL)

    def search_bar(self):
        return self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/header/div/div/div/div/form/input")

    def search_button(self):
        return self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/header/div/div/div/div/form/button")

    def consent_x_button(self):
        return self.driver.find_element_by_xpath("/html/body/div[3]/div[8]/div/div[2]/div/button/img")
