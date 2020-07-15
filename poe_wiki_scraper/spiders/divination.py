import scrapy
import json
import requests

import os


class DivinationScraper(scrapy.Spider):
    name = "divination"

    start_urls = ["https://pathofexile.gamepedia.com/Divination_card"]

    def get_map_name(self, poe_map):
        return poe_map.strip().replace("[[", "").replace("]]", "").split("|")[0]

    def parse_maps(self, td):
        if td is None:
            return None

        return [self.get_map_name(x) for x in td.split("•")]


    def parse(self, response):
        data = []

        res = response.css(".item-table tbody tr")


        for row in res:
            name = None
            stack_size = None
            drop_areas = None
            drop_restrictions = None

            td_xpath = row.xpath(".//td")

            if len(td_xpath) == 5:
                name = td_xpath[0].xpath(".//a/@title").get()
                stack_size = td_xpath[1].xpath("./@data-sort-value").get()
                drop_areas = self.parse_maps(td_xpath[3].xpath("./@data-sort-value").get())
                drop_restrictions = td_xpath[4].xpath("./@data-sort-value").get()
                drop_restrictions = drop_restrictions.replace("[[", "").replace("]]", "") if drop_restrictions is not None else None

            if name != None:
                data.append({
                    "name": name,
                    "stack_size": int(stack_size) if stack_size is not None else None,
                    "drop_areas": drop_areas,
                    "drop_restrictions": drop_restrictions
                })


        with open("data/divination.json", "w") as divination_json:
            divination_json.write(json.dumps(data))

