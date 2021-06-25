from typing import List, Dict

from constants import Shop
from scraper.base.article_subscriber import ArticleSubscriber
from scraper.base.base_article import BaseArticle
from scraper.shops.bike_components import BikeComponents


class Scraper(ArticleSubscriber):
    def __init__(self) -> None:
        self.subscribers: List[ArticleSubscriber] = []

        self.bike_components = BikeComponents()
        self.bike_components.add_subscriber(self)

    def on_change(self, available: bool, shop: Shop, article: BaseArticle) -> None:
        for subscriber in self.subscribers:
            subscriber.on_change(available, shop, article)

    def watch_article(self, article: BaseArticle):
        self.bike_components.watch(article)

    def add_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.remove(subscriber)
