import scrapy


class SubtitleSpider(scrapy.Spider):
    name = "subtitle"
    start_urls = ["https://www.opensubtitles.org/en/search2/sublanguageid-all/moviename-arrow"]

    def parse(self, response):
        css_class = "bnone"
        img_title = "TV Series"
        for search in response.xpath("//td"):
            title = search.xpath(".//a[contains(@class, $css)]/text()", css=css_class).extract_first()
            url = search.xpath(".//a[contains(@class, $css)]/@href", css=css_class).extract_first()
            img = search.xpath(".//img[contains(@title, $title)]/@title", title=img_title).extract_first()
            if title and url and img:
                yield {
                    "title": title,
                    "url": url
                }
