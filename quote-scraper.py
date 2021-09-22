import scrapy
import html2text
import re

######################################
## Adicione quantos autores desejar ##

authors = [
                '4.Douglas_Adams',
                '22782.George_Carlin',
                '16667.Isaac_Asimov'
            ]

######################################


domain = 'https://www.goodreads.com'

class GoodreadsSpider(scrapy.Spider):
    name = "goodreads_spider"
    start_urls = []

    def __init__(self, **kwargs):
        print (**kwargs)
        urls = []
        for author in authors:
            url_complete = domain + '/author/quotes/' + author
            urls.append(url_complete)
        
        self.start_urls = urls
        super().__init__(**kwargs) 


    def parse(self, response):
        SET_SELECTOR = '.quoteText'
        AUTHOR_SELECTOR = '.authorOrTitle::text'
        BOOK_SELECTOR = 'span a ::text'
        QUOTE_SELECTOR = '.quoteText::text'
        
        for quote in response.css(SET_SELECTOR):
            
            author = quote.css(AUTHOR_SELECTOR).extract_first()
            book = quote.css(BOOK_SELECTOR).extract_first()

            text_raw = quote.css(QUOTE_SELECTOR).extract()
            text_concat = " ".join(text_raw)  
            text_pre_sanitized = html2text.html2text(text_concat)
            regex = r'\“(.+?)\”'
            matches = re.match(regex, text_pre_sanitized, re.DOTALL)
            
            if matches:
                text_sanitized = matches.group()
            else:
                text_sanitized = text_pre_sanitized

            yield {
                'text': text_sanitized,
                'author': author,
                'book': book,
            }

        NEXT_PAGE_SELECTOR = '.next_page::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        
        if next_page:
            next_page = domain + next_page
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
