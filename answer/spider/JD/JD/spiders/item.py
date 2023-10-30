import scrapy
from items import ProductItem
class ItemSpider(scrapy.Spider):
    name = "item"
    allowed_domains = ["jd.com"]
    start_urls = ["https://list.jd.com/list.html?cat=1318,12099,9756"]
    def start_requests(self):  # 重写start_requests方法来实现post请求
        url = self.start_urls[0]
        # 构建post请求
        yield scrapy.Request(
            url=url,
            method='GET',
            callback=self.parse,
            headers={'Content-Type': 'application/json'}
        )
    def parse(self, response):
        resjson=[]
        productItem = ProductItem()
        for gl in response.css('li.gl-item'):
            productItem['title']=response.xpath('/html/head/title')
            productItem['name'] = gl.css('.p-name em::text').extract_first().strip()
            productItem['sku'] = int(gl.xpath('div[@class="gl-i-wrap j-sku-item"]//@brand_id').extract_first())
            productItem['img_urls'] = gl.css('div.p-img img::attr(data-lazy-img)').extract_first()
            productItem['detail'] = "//item.jd.com/" + str(productItem['id']) + ".html"
            resjson.append(productItem)
            yield productItem
        file=open("res.json","w")
        file.write(resjson)
        file.close()