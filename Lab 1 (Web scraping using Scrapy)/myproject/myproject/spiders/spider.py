import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/']
    max_pages = 5

    def parse(self, response):
        page = response.meta.get('page', 1)
        books = response.css('article.product_pod')

        for book in books:
            book_url = book.css('h3 a::attr(href)').get()
            if book_url:
                yield response.follow(
                    book_url,
                    self.parse_book_details,
                    meta={'page': page}
                )

        if page < self.max_pages:
            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                yield response.follow(
                    next_page,
                    self.parse,
                    meta={'page': page + 1}
                )

    def parse_book_details(self, response):
        product_url = response.url
        page = response.meta.get('page', 1)

        title = response.css('h1::text').get()
        price = response.css('p.price_color::text').get()

        rating_class = response.css('p.star-rating::attr(class)').get()
        if rating_class:
            rating = rating_class.split()[-1]
        else:
            rating = None

        availability = response.css('p.instock.availability::text').getall()
        if availability:
            availability = ''.join(availability).strip()
        else:
            availability = None

        description = response.css('div#product_description + p::text').get()

        upc = response.css('table.table tbody tr td::text').get()

        rows = response.css('table.table tbody tr')
        for row in rows:
            label = row.css('th::text').get()
            if label and 'UPC' in label:
                upc = row.css('td::text').get()
                break

        number_of_reviews = None
        for row in rows:
            label = row.css('th::text').get()
            if label and 'Number of reviews' in label:
                number_of_reviews = row.css('td::text').get()
                break

        category = response.css('ul.breadcrumb li:nth-last-child(2) a::text').get()

        yield {
            'page': page,
            'product_url': product_url,
            'title': title,
            'category': category,
            'price': price,
            'rating': rating,
            'availability': availability,
            'description': description,
            'upc': upc,
            'number_of_reviews': number_of_reviews,
        }