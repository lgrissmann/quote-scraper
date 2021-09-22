Crawler em Python, baseado [neste excelente artigo](https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt), que busca frases de autores específicos no site [Goodreads](https://www.goodreads.com/)


Procure no site Goodreads os autores de interesse copiando a última parte do *path* composta pelo `id.nome_do_autor`

Exemplo, caso a url seja: https://www.goodreads.com/author/show/22782.George_Carlin

A parte que interessa é **22782.George_Carlin**

Adicione quantos autores quiser[^1] à variável `authors`. 

[^1]: Lembre-se: Quanto mais autores você adicionar, mais tempo a operação vai levar.

```
authors = [
            '4.Douglas_Adams',
            '22782.George_Carlin',
            '16667.Isaac_Asimov'
            ]
```

Para rodar:

```python3
scrapy runspider quote-scraper.py -o quotes.json
```