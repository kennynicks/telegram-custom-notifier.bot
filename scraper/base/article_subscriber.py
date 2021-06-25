from constants import Shop
from scraper.base.base_article import BaseArticle


class ArticleSubscriber:
    def on_change(self, available: bool, shop: Shop, article: BaseArticle) -> None:
        raise NotImplementedError()
