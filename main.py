from bot.bot import Bot
from constants import Shop
from scraper.articles.test_article import TestArticle
from scraper.base.article_subscriber import ArticleSubscriber
from scraper.base.base_article import BaseArticle
from scraper.scraper import Scraper


class Main(ArticleSubscriber):
    def on_change(self, available: bool, shop: Shop, article: BaseArticle) -> None:
        print("{}: {}".format(article.name, available))

    def run(self):
        print("running")
        bot = Bot()
        scraper = Scraper()
        scraper.watch_article(TestArticle())
        scraper.add_subscriber(self)
        bot.run()


if __name__ == '__main__':
    Main().run()
