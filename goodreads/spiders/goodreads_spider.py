import scrapy
import html2text
import re

def simple_sanitize(raw):
    text_sanitized = ''
    if raw:
        text_sanitized = re.sub('[^a-zA-Z ]', '', raw)
        
    return text_sanitized.strip()

def text_sanitize(raw):
    text_pre_sanitized = html2text.html2text(raw)
    regex = r'\“(.+?)\”'
    matches = re.match(regex, text_pre_sanitized, re.DOTALL)
    if matches:
        return matches.group()
    else:
        return text_pre_sanitized
    

class GoodreadsSpiderSpider(scrapy.Spider):
    name = 'goodreads_spider'
    allowed_domains = ['www.goodreads.com']
    domain = 'https://www.goodreads.com'
    follow_next = False

    def start_requests(self):           
        start_url = getattr(self, 'url', None)    
        self.follow_next = getattr(self, 'follow-next', False) 
        yield scrapy.Request(start_url, self.parse)


    def parse(self, response):
        SET_SELECTOR = '.quoteText'
        AUTHOR_SELECTOR = '.authorOrTitle::text'
        BOOK_SELECTOR = 'span a ::text'
        QUOTE_SELECTOR = '.quoteText::text'
        
        for quote in response.css(SET_SELECTOR):
            
            author = quote.css(AUTHOR_SELECTOR).extract_first()
            author = simple_sanitize("".join(author))

            book = simple_sanitize(quote.css(BOOK_SELECTOR).extract_first())

            text_raw = quote.css(QUOTE_SELECTOR).extract()
            text_sanitized = text_sanitize(" ".join(text_raw))

            yield {
                'text': text_sanitized,
                'author': author,
                'book': book,
            }

        if self.follow_next:
            next_page = response.css('.next_page::attr(href)').extract_first()
            if next_page:
                next_page = self.domain + '/' + next_page
                print(next_page)
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
