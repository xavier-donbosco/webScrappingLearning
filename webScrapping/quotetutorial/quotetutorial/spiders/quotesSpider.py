import scrapy

from .. import items
from ..items import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls=[
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response, **kwargs):

        items=QuotetutorialItem()

        all_quotes=response.css("div.quote")

        for i in all_quotes:
            title=i.css("span.text::text").extract()
            author=i.css("small.author::text").extract()
            tags=i.css("a.tag::text").extract()

            items['title']=title
            items['author'] = author
            items['tag'] = tags

            yield items

        next_page=response.css("li.next a::attr(href)").get()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)