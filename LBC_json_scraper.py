import scrapy
import json

'''''Scrapy spider - real estate market scraping
This scraper fetch liens from json file (LBC_research_scraper.py output) and scrap data
Before launching : set filename.json
terminal -> § scrapy runspider LBC_json_scraper.py -o output_filename.json
'''

class LBCSpider(scrapy.Spider):
    name = "LBC_json_scraper"
    start_urls = []
    with open('filename.json') as f:    # insert filename.json file here
        liste_annonces = json.load(f)
        for ann in liste_annonces:
            url_to_add = 'https://www.leboncoin.fr'+ann['lien_annonce']
            start_urls.append(url_to_add)

    def parse(self, response):
        for annonce in response.css('section._1_H-h'):
            yield {
                'nom': annonce.xpath('div[1]/div/div/div/div[1]/div[1]/span/text()').extract_first(),
                'baseline': annonce.xpath('div[1]/div/div/div/div[1]/div[2]/ul/li[1]/span/text()').extract_first(),
                'SIREN': annonce.xpath('div[1]/div/div/div/div[1]/div[2]/ul/li[5]/div/text()[2]').extract_first(),
                'adresse': annonce.xpath('div[1]/div/div/div/div[1]/div[2]/ul/li[1]/div/text()').extract_first(),
                }
