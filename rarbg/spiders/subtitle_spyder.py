import scrapy


class SubtitleSpider(scrapy.Spider):
    name = "subtitle"
    start_urls = ["https://www.opensubtitles.org/en/search2/sublanguageid-all/moviename-arrow"]

    def parse(self, response):
        for search in response.css("#search_results a.bnone"):
            yield {
                "title": search.css("a::text").extract_first(),
                "url": search.css("a::attr(href)").extract_first(),
            }