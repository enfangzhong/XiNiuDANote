import scrapy
from TravelInfo.items import FindtripItem

class QuaSpider(scrapy.Spider):
    name = "Qua"
    start_urls = [
        "http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2017-07-21&searchArrivalTime=2017-07-23&nextNDays=0&startSearch=true&fromCode=BJS&toCode=SHA&from=qunarindex&lowestPrice=null"
    ]

    def parse(self, response):
        dataList = response.xpath('//div[@class="mb-10"]/div[@class="m-airfly-lst"]/div[@class="b-airfly"]')
        #print dataList
        items = []

        for index,flight in enumerate(dataList):

            leave_airports = " ".join(flight.xpath('.//div[@class="sep-lf"]/p[@class="airport"]/span/text()').extract())
            arrive_airports = " ".join(flight.xpath('.//div[@class="sep-rt"]/p[@class="airport"]/span/text()').extract())
            #company = flight.xpath('.//div[@class="col-airline"]/div/span/text()').extract_first()
            plane_type = flight.xpath('.//div[@class="num"]/span/text()').extract()
            flight_leave_time = flight.xpath('.//div[@class="sep-lf"]/h2/text()').extract_first()
            flight_arrive_time = flight.xpath('.//div[@class="sep-rt"]/h2/text()').extract_first()
            passtime = flight.xpath('.//div[@class="sep-ct"]/div[@class="range"]/text()').extract_first()
            price = flight.xpath('.//div[@class="col-price"]/h2/text()').extract_first()
            discount = flight.xpath('.//span[@class="v dis"]/text()').extract_first()

            print "".join(leave_airports) +' --> '+"".join(arrive_airports)
            #print "".join(company)
            print "".join(plane_type)
            print "".join(flight_leave_time)
            print "".join(flight_arrive_time)
            print "".join(passtime)
            print price
            print "".join(discount)
            print "\n"

            item = FindtripItem()
            item['site'] = 'Qua'
            #item['company'] = "".join(company)
            item['flight_time'] = "".join(flight_leave_time) + "-->" + "".join(flight_arrive_time)
            item['airports'] = "".join(leave_airports) +' --> '+"".join(arrive_airports)
            item['passtime'] = "".join(passtime)
            item['price'] = price
            item['discount'] = "".join(discount)
            items.append(item)
        return items
