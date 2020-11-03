import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from Dev.Pages.AllegroHomePage import AllegroHomePage
from Dev.Pages.AllegroSearchPage import AllegroSearchPage

def xpathExtractor(driver, element):
    return str(driver.execute_script("gPt=function(c){if(c.id!==''){return'id(\"'+c.id+'\")'}if(c===document.body)"
                                     "{return c.tagName}var a=0;var e=c.parentNode.childNodes;for(var b=0;b<e.length;"
                                     "b++){var d=e[b];if(d===c){return gPt(c.parentNode)+'/'+c.tagName.toLowerCase()+"
                                     "'['+(a+1)+']'}if(d.nodeType===1&&d.tagName===c.tagName){a++}}};return "
                                     "gPt(arguments[0]);", element))


opts = Options()
# opts.set_headless(True)

#Gecko driver path is required if not added to PATH
driver = webdriver.Firefox(executable_path='D:\\SamplePageObjectModelProject\\Drivers\\geckodriver.exe')
driver.implicitly_wait(3)

# home_page = AllegroHomePage(driver)
# home_page.navigate_to_url()
search_page = AllegroSearchPage(driver)
search_page.navigate_to_url()

elements_list = driver.find_elements(By.XPATH, "//*[@class]")

#Output path for mapping file
mappingFile = open('\\PycharmProjects\\Allegro\\search_page_mapping.py', 'w')
xpathList = []
time.sleep(5)
for element in elements_list:
    try:
        if element.get_attribute('name') is not None:
            if element.get_attribute('name') != "":
                xpathList += ("\tdef " + element.get_attribute('name') + "_" + element.tag_name + "(self):\n"
                + "\t\treturn self.driver.find_element_by_xpath(\"" + xpathExtractor(driver, element).replace("\"", "\\\"") + "\")\n\n")
            elif element.tag_name != "img":
                if element.tag_name == "a":
                    xpathList += ("\tdef " + str(element.get_attribute('class')).replace(" ", "_").replace("-", "_") + "_link" "(self):\n"
                                      + "\t\treturn self.driver.find_element_by_xpath(\"" + xpathExtractor(driver, element).replace("\"", "\\\"") + "\")\n\n")
                else:
                    xpathList += ("\tdef " + str(element.get_attribute('class')).replace(" ", "_").replace("-", "_") + "_" + element.tag_name + "(self):\n"
                                      + "\t\treturn self.driver.find_element_by_xpath(\"" + xpathExtractor(driver, element).replace("\"", "\\\"") + "\")\n\n")
    except selenium.common.exceptions.StaleElementReferenceException as e:
        print(e)
for line in xpathList:
    mappingFile.write(line)
mappingFile.close()
driver.close()
