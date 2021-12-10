



import urllib, os, platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver_options = webdriver.firefox.options.Options()
driver_options.add_argument('--headless')
driver_options.add_argument("--disable-gpu")

if platform.system() == "Linux":
    execpath = "geckodriver"
elif platform.system() == "Windows":
    execpath = "C:/Users/jiwoo/geckodriver.exe"
else:
    raise Exception("remember to add geckodriver executable to PATH, me.")



class ScrapedPage():
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Firefox(executable_path = execpath, options=driver_options)
        self.browser.get(url)
       #self.text = urllib.requests.urlopen(self.url).read() 
       #self.soup = BeautifulSoup(self.text, "lxml")
    def quit(self):
        self.browser.quit()
    def reopen_page(self):
        self.browser = webdriver.Firefox(executable_path = execpath, options=driver_options)
        self.browser.get(self.url)

class CovidScraper(ScrapedPage):
    def __init__(self, url='https://www.gov.sg/features/covid-19'):
        print("launch")
        super().__init__(url)
        print("super init")
        self.covid_box = self.browser.find_element_by_css_selector("div.feature-intro.content")
        print("got box")
      # self.covidupdate = self.soup.find_all(class_="feature-intro__content")
    def getcontents(self):
        return self.covid_box.text



        