# -*- coding: utf-8 -*-
import scrapy


class OlxSpider(scrapy.Spider):
    name = 'olx'
    allowed_domains = ['www.olx.ro']
    start_urls = ['https://www.olx.ro/imobiliare/apartamente-garsoniere-de-inchiriat/1-camera/cluj-napoca/']

    def parse(self, response):

        #TODO: Take the date
        #TODO: Move to NEXT PAGE
        #TODO: Take title
        columns = response.css('#offers_table')
        columns = response.css('table[id="offers_table"] > tbody > tr[class="wrap"]')
        for col in columns:
            # Get the required text from element.
            yield {
                "price": col.css("td[class='wwnormal tright td-price'] div > p > strong::text").extract_first()
                # "title": col.css("td[class='titleColumn'] a::text").extract_first(),
                # "year": col.css("td[class='titleColumn'] span::text").extract_first().strip("() "),
                # "rating": col.css("td[class='ratingColumn imdbRating'] strong::text").extract_first(),
            }