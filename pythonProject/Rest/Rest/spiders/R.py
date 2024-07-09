import json
from prettytable import PrettyTable
import scrapy
from scrapy import Request


class RSpider(scrapy.Spider):
    name = "R"

    def start_requests(self):
        yield Request(
            url = 'https://restcountries.com/v3.1/all',
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.text)
        t = PrettyTable(['Country', 'Capital', 'Flag URL'])
        # print(len(data))
        for i in data:
            try:
                each_name = i['name']["common"]
            except:
                each_name =''
            try:
                each_capital = (str(i['capital']).replace('[','').replace(']','').
                                replace("'",''))
            except:
                each_capital = ''
            try:
                each_flag = i["flags"]['png']
            except:
                each_flag = ''
            t.add_row([each_name, each_capital,each_flag])
        print(t)

