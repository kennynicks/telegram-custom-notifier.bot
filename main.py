from bot.bot import Bot
from constants import Shop
from scraper.articles.n03a_article import N03A
from scraper.base.article_subscriber import ArticleSubscriber
from scraper.base.base_article import BaseArticle
from scraper.scraper import Scraper


class Main(ArticleSubscriber):

    def __init__(self):
        self.scraper = Scraper()
        self.scraper.add_subscriber(self)
        self.bot = Bot(self.scraper)

    def on_change(self, available: bool, shop: Shop, article: BaseArticle) -> None:
        message = "*[{}]({}):*\n_{}_".format(article.name, article.article_entries[shop],
                                             "Is available" if available else "Not available")
        self.bot.send_message(message)

    def run(self):
        print("running main")
        self.scraper.watch_article(N03A())
        self.bot.run()


if __name__ == '__main__':
    Main().run()
