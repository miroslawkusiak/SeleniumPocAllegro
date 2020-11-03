from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from Dev.Pages.AllegroHomePage import AllegroHomePage
from Dev.Pages.AllegroSearchPage import AllegroSearchPage

opts = Options()
# opts.set_headless(True)

'''Gecko driver path is required if not added to PATH'''
driver = webdriver.Firefox(executable_path='D:\\SamplePageObjectModelProject\\Drivers\\geckodriver.exe')
driver.implicitly_wait(10)

home_page = AllegroHomePage(driver)
search_page = AllegroSearchPage(driver)

print("======================= 1. Navigate to www.allegro.pl .")
home_page.navigate_to_url()
print("======================= 2. Search Iphone 11.")
home_page.consent_x_button().click()
home_page.search_bar().send_keys("Iphone 11")
home_page.search_button().click()
print("======================= 3. Select black colour.")
search_page.black_color_selection().click()
print("======================= 4. Get number of displayed items.")

offerslisting = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/div[3]")
articles = offerslisting.find_elements_by_tag_name("article")
print(">Number of offerings: " + str(len(articles)))

prices = driver.find_elements_by_xpath("//div[2]/div[2]/div/div/span")
formatted_prices = []
for price in prices:
    formatted_prices.append(
        float(str(price.get_attribute("innerText")).replace("zł", "").replace(" ", "").replace(",", ".")))

print("======================== 5. Get Highest price.")
print(">Highest price: " + str(max(formatted_prices)) + " zł")
print("========================  6. Get Highest price + 23% tax")
print(">Highest price with VAT: " + str(round(max(formatted_prices) * 1.23, 2)) + " zł")

