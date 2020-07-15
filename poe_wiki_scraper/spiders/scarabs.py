import scrapy
import json
import requests

import os


class ScarabScraper(scrapy.Spider):
    name = "scarab"

    start_urls = ["https://pathofexile.gamepedia.com/Scarab"]

    try:
        os.makedirs("data/images/scarab")
    except OSError:
        pass

    def extract_image_and_name(self, td):
        image_selector = td.xpath(".//img/@src").get()
        name = td.xpath(".//a/@title").get()

        image_response = requests.get(image_selector).content

        image = "{}.png".format(name.replace(" ", "-").replace("'", "").lower())

        with open("data/images/scarab/{}".format(image), "wb") as image_handler:
                     image_handler.write(image_response)

        return [name, image]


    def parse(self, response):
        data = []

        res = response.css(".item-table tbody tr")

        for row in res:
            name = None
            stats = None
            image = None

            td_xpath = row.xpath(".//td")

            if len(td_xpath) == 2:
                [name, image] = self.extract_image_and_name(td_xpath[0])
                stats = td_xpath[1].xpath("./@data-sort-value").get()

            if name != None:
                data.append({
                    "name": name,
                    "image": image,
                    "stats": stats
                })


        with open("data/scarab.json", "w") as scarab_json:
            scarab_json.write(json.dumps(data))

