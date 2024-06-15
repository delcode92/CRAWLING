import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options


class SeleniumSpider(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = ['https://diskominfo.acehprov.go.id']

    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Firefox(options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(5)  # Wait for the JavaScript to load

        links = self.driver.find_elements(By.XPATH, "//a[@href]")
        urls = [link.get_attribute('href') for link in links]

        for url in urls:
            if url:
                yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        # Process the details page
        self.log(f'Visited: {response.url}')
        # Extract data from the page as needed

    def closed(self, reason):
        self.driver.quit()

