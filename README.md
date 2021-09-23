Crawler em Python, baseado [neste excelente artigo](https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt) e na [documentação oficial do Scrapy](https://docs.scrapy.org/en/latest/index.html), para busca de citações ([quotes](https://www.goodreads.com/quotes)).

## Como usar
```nash
$ scrapy crawl goodreads_spider -a url=<URL_INICIAL> [-a follow-next=True|False]
```

- *url*: Navegue pelo site www.goodreads.com para encontrar qual página você deseja como ponto de partida.
- *follow-next*: O padrão é `False`


## Exemplos

1. Buscar todas as frases do Frank Zappa
    ```
    scrapy crawl goodreads_spider -a url=https://www.goodreads.com/author/quotes/22302.Frank_Zappa -a follow-next=True
    ```

1. Buscar apenas a primeira página das frases de humor

    ```
    scrapy crawl goodreads_spider -a url=https://www.goodreads.com/quotes/tag/humor
    ```