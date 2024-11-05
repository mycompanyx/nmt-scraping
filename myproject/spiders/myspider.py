import scrapy
# https://learning.aljazeera.net/       
                
import scrapy

class AlJazeeraSpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://learning.aljazeera.net/en/lessons/level/beginner"] 
    #https://learning.aljazeera.net/en/lessons/level/intermediate
    # https://learning.aljazeera.net/en/lessons/level/intermediate

    def parse(self, response):
        # Select each nested div within the "view-content" div
        content_divs = response.xpath('//div[@class="view-content"]/div')

        for div in content_divs:
            # Extract all a tags within h4 elements inside the div
            links = div.xpath('.//h4[@class="field-content"]/a')
            url = 'https://learning.aljazeera.net'

            for link in links:
                # Extract the href attribute of each a tag and concatenate with the base URL
                relative_url = link.xpath('@href').get()
                full_url = url + relative_url
                link_text = link.xpath('text()').get()

                # Pass the full URL and link text to parse_content
                yield response.follow(full_url, callback=self.parse_content, meta={'link_text': link_text, 'url': full_url})

    def parse_content(self, response):
        # Extract the link text and URL from the meta dictionary
        link_text = response.meta['link_text']
        url = response.meta['url']

        # Extract the main content on the linked page (customize the XPath as needed)
        page_content = response.xpath('//div[@class="original-body body-text field field--name-body field--type-text-with-summary field--label-hidden field--item"]//text()').getall()
        
        # Join all text content from the div
        page_content = " ".join(page_content).strip()

        yield {
            "link_text": link_text,
            "url": url,
            "page_content": page_content,
        }
