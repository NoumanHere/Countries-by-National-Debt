# -*- coding: utf-8 -*-
import scrapy


class GdpSpider(scrapy.Spider):
    name = 'GDP'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath('//tr')
        for country in countries:
            name = country.xpath('.//td[1]/a/text()').get()
            gdp = country.xpath('.//td[2]/text()').get()
            population = country.xpath('.//td[3]/text()').get()

            yield{
                'Country_name':name,
                'Gdp_dept':gdp,
                'Population':population
            }

