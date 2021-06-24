from scraper.base.base_article import BaseArticle, ArticleEntry


class ArticleSubscriber:
    def on_change(self, available: bool, shop: ArticleEntry, article: BaseArticle) -> None:
        raise NotImplementedError()
