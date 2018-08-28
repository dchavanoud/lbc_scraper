import scrapy

'''Scrapy spider - real estate market scraping
Before launching : set LBC urls (caegory, cities, etc.) and page_number
terminal -> § scrapy runspider LBC_research_scraper.py -o filename.json
output : filename.json (titre, lien_annonce, prix, vendeur, date de publication)

* catref :
vente immobilière : 9
location : 10
* regionref :
Rhone-Apes : 9
* cityref :
Lyon : Lyon
Lyon 6 : Lyon_69006
'''

class LBCSpider(scrapy.Spider):
    name = "LBC_research_scraper"
    base_url = 'https://www.leboncoin.fr/recherche/?category='catref'&regions='regionref'&cities='cityref''.    #personalize url before launching
    page_number =     #how many pages de we want to scrap?
    start_urls = []
    for page in range(page_number):
        url_to_add = base_url + "&page=" + str(page+1)
        start_urls.append(url_to_add)

    def parse(self, response):
        for annonce in response.css('li._3DFQ-'):
            yield {
                'titre': annonce.css('a::attr("title")').extract_first(),
                'lien_annonce': annonce.css('a::attr("href")').extract_first(),
                'prix': annonce.xpath('a/section/div[2]/div[1]/span/span/text()').extract_first(),
                'vendeur': annonce.xpath('a/section/div[1]/p[1]/span/text()').extract_first(),
                'date_publication': annonce.xpath('a/section/div[2]/div[2]/div/text()').extract_first(),
                }

