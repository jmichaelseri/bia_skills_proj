import scrapy

class BiSpider(scrapy.Spider):
    name = "jobs"
    
    start_urls = [
        "https://www.glassdoor.co.uk/Job/cardiff-business-intelligence-analyst-jobs-SRCH_IL.0,7_IC3300986_KO8,37.htm?radius=100"
    ]
    
    def parse(self, response):
        for job in response.xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[1]/text()'):

            yield {
                'employer': 
                }
            
   