from scrapy import cmdline

cmdline.execute("scrapy crawl subtitle -o sub.json".split())