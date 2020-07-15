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

    def extract_image_and_name(self, td):
        image_selector = td.xpath(".//img/@src").get()
        name = td.xpath(".//a/@title").get()

        image_response = requests.get(image_selector).content

        image = "{}.png".format(name.replace(" ", "-").replace("'", "").lower())

        with open("data/images/currency/{}".format(image), "wb") as image_handler:
                     image_handler.write(image_response)

        return [name, image]


    def parse(self, response):
        data = []

        res = response.css(".item-table tbody tr")


        for row in res:
            name = None
            image = None
            drop_level = None
            stack_size = None
            tab_stack_size = None
            help_text = None


            td_xpath = row.xpath(".//td")


            if len(td_xpath) == 4:
                [name, image] = self.extract_image_and_name(td_xpath[0])
                drop_level = td_xpath[1].xpath("./@data-sort-value").get()
                effects = td_xpath[2].xpath(".//@data-sort-value").get()
                help_text = td_xpath[3].xpath(".//@data-sort-value").get()
            elif len(td_xpath) == 5:
                [name, image] = self.extract_image_and_name(td_xpath[0])
                drop_level = td_xpath[1].xpath("./@data-sort-value").get()
                stack_size = td_xpath[2].xpath("./@data-sort-value").get()
                tab_stack_size = td_xpath[3].xpath("./@data-sort-value").get()
                help_text = td_xpath[4].xpath("./@data-sort-value").get()


            if name != None:
                data.append({
                    "name": name,
                    "image": image,
                    "drop_level": int(drop_level) if drop_level is not None else None,
                    "stack_size": int(stack_size) if stack_size is not None else None,
                    "tab_stack_size": int(tab_stack_size) if tab_stack_size is not None else None,
                    "help_text": help_text
                 })

        with open("data/currency.json", "w") as currency_json:
            currency_json.write(json.dumps(data))

