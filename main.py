from bot.bot import Bot
from scraper.articles.test_article import TestArticle
from scraper.base.article_subscriber import ArticleSubscriber
from scraper.scraper import Scraper


class Main(ArticleSubscriber):
    def run(self):
        print("running")
        bot = Bot()
        scraper = Scraper()
        scraper.watch_article(TestArticle())
        scraper.add_subscriber(self)
        bot.run()


if __name__ == '__main__':
    Main().run()
