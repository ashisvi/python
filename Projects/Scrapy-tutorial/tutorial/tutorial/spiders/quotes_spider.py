from pathlib import Path

import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quotes = []
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.json"

        for quote in response.css("div.quote"):
            quotes.append(
                {
                    "quote": response.css("span.text::text").get(),
                    "author": response.css("small.author::text").get(),
                    "tags": response.css("div.tags a.tag::text").getall(),
                }
            )
        Path(filename).write_bytes(
            json.dumps(quotes, ensure_ascii=False).encode("utf-8")
        )
        self.log(f"Saved file {filename}")
