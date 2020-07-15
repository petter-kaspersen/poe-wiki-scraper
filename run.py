import scrapy
from scrapy.crawler import CrawlerProcess
import os

from scrapy.utils.project import get_project_settings

try:
    os.makedirs("data")
except OSError:
    pass



process = CrawlerProcess(get_project_settings())

process.crawl('currency')
process.crawl("divination")
process.crawl("scarabs")

process.start()