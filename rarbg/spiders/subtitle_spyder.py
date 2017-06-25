import scrapy


class SubtitleSpider(scrapy.Spider):
    name = "subtitle"
    start_urls = ["https://www.opensubtitles.org/en/search2/sublanguageid-all/moviename-arrow"]

    def parse(self, response):
        img_title = "TV Series"
        for search in response.xpath("//td"):
            title = search.css("a.bnone::text").extract_first()
            url = search.css("a.bnone::attr(href)").extract_first()
            img = search.css("img::attr(title)").extract_first()
            if title and url and img == img_title:
                yield {
                    "title": title,
                    "url": url
                }