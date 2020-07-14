import scrapy
import json
import requests

import os


class CurrencyScraper(scrapy.Spider):
    name = "currency"

    start_urls = ["https://pathofexile.gamepedia.com/Currency"]

    try:
        os.makedirs("data/images/currency")
    except OSError:
        pass


    def parse(self, response):
        data = []

        res = response.css(".c-item-hoverbox__activator")

        for row in res:
            image = row.xpath(".//img/@src").get()
            name = row.xpath(".//a/@title").get()

            image_response = requests.get(image).content

            image_name = "{}.png".format(name.replace(" ", "-").replace("'", "").lower())

            with open("data/images/currency/{}".format(image_name), "wb") as image_handler:
                image_handler.write(image_response)

            is_inside = [x for x in data if x["name"] == name]

            if len(is_inside) <= 0:
                data.append({
                    "image": image_name,
                    "name": name
                })

        with open("data/currency.json", "w") as currency_json:
            currency_json.write(json.dumps(data))