import scrapy
from TravelInfo.items import FindtripItem

class CtripSpider(scrapy.Spider):
    name = "Ctrip"
    start_urls = [
        "http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2017-07-27"
    ]

    def parse(self, response):
        dataList = response.xpath("//div[@id='J_flightlist2']/div")
        #print dataList
        items = []

        for index,flight in enumerate(dataList):

            company = flight.xpath('.//div[@class="clearfix J_flight_no"]/strong/text()').extract_first()
            leave_airports = flight.xpath('.//tr[@class="J_header_row"]/td[@class="right"]/div[2]/text()').extract_first()
            flight_leave_time = flight.xpath('.//tr[@class="J_header_row"]/td[@class="right"]/div[1]/strong/text()').extract_first()
            arrive_airports = flight.xpath('.//tr[@class="J_header_row"]/td[@class="left"]/div[2]/text()').extract_first()
            flight_arrive_time = flight.xpath('.//tr[@class="J_header_row"]/td[@class="left"]/div[1]/strong/text()').extract_first()
            price = flight.xpath('.//td[@class="price "]/span/span/text()').extract_first()
            plane_type = flight.xpath('.//span[@data-bit="FlightType"]/text()').extract_first()


            print leave_airports
            print arrive_airports
            print company
            print plane_type
            print flight_leave_time
            print flight_arrive_time
            print price
            print "\n"

            try:
                item = FindtripItem()
                item['site'] = 'Ctrip'
                item['company'] = company
                item['flight_time'] = flight_leave_time + "-->" + flight_arrive_time
                item['airports'] = leave_airports +' --> ' + arrive_airports
                item['plane'] = plane_type
                item['price'] = price
                items.append(item)
            except:
                pass
        return items
