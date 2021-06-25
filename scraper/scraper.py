from typing import List, Dict

from constants import Shop
from scraper.base.article_subscriber import ArticleSubscriber
from scraper.base.base_article import BaseArticle
from scraper.shops.amazon import Amazon
from scraper.shops.bike_24 import Bike24
from scraper.shops.bike_components import BikeComponents
from scraper.shops.bike_discount import BikeDiscount


class Scraper(ArticleSubscriber):
    def __init__(self) -> None:
        self.subscribers: List[ArticleSubscriber] = []

        self.bike_components = BikeComponents()
        self.bike_discount = BikeDiscount()
        self.bike_24 = Bike24()
        self.amazon = Amazon()
        self.bike_components.add_subscriber(self)
        self.bike_discount.add_subscriber(self)
        self.bike_24.add_subscriber(self)
        self.amazon.add_subscriber(self)

    def on_change(self, available: bool, shop: Shop, article: BaseArticle) -> None:
        for subscriber in self.subscribers:
            subscriber.on_change(available, shop, article)

    def watch_article(self, article: BaseArticle):
        if Shop.BIKE_COMPONENTS in article.article_entries:
            self.bike_components.watch(article)
        if Shop.BIKE_DISCOUNT in article.article_entries:
            self.bike_discount.watch(article)
        if Shop.BIKE_24 in article.article_entries:
            self.bike_24.watch(article)
        if Shop.AMAZON in article.article_entries:
            self.amazon.watch(article)

    def add_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.remove(subscriber)
