from typing import List

from scraper.base.article_subscriber import ArticleSubscriber
from scraper.base.base_article import BaseArticle


class BaseShopScraper:
    def __init__(self):
        self.subscribers: List[ArticleSubscriber] = []

    def watch(self, article: BaseArticle):
        raise NotImplementedError()

    def add_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.remove(subscriber)
