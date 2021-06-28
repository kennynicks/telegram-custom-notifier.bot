from __future__ import annotations

import logging
import os
from typing import List

from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater, CommandHandler, CallbackQueryHandler, CallbackContext
)

from scraper.scraper import Scraper

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, scraper: Scraper) -> None:
        self.updater = Updater(os.getenv("BOT_TOKEN"))
        self.scraper = scraper

    def send_message(self, chat_message: str, parse_mode: ParseMode = ParseMode.MARKDOWN_V2) -> None:
        self.updater.bot.sendMessage(os.getenv("CHAT_ID"), chat_message, parse_mode=parse_mode)

    def status(self, update: Update, context: CallbackContext) -> None:
        print(self.scraper.get_status())
        self.send_message(self.scraper.get_status())

    def button_clicked(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        switcher = {"status": lambda: self.status(update, context)}
        switcher.get(query.data)()

    def start(self, update: Update, context: CallbackContext) -> None:
        """Sends a message with 5 inline buttons attached."""
        update.message.reply_text(text="Menu:",
                                  reply_markup=self.build_keyboard())

    def build_keyboard(self) -> InlineKeyboardMarkup:
        buttons: List[InlineKeyboardButton] = [InlineKeyboardButton("Status", callback_data="status")]
        return InlineKeyboardMarkup.from_column(buttons)

    def run(self) -> None:
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.button_clicked))
        dispatcher.add_handler(CommandHandler("status", self.status))
        self.updater.start_polling()
        self.updater.idle()
