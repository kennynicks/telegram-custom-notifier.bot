from __future__ import annotations
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    ContextTypes,
    CallbackQueryHandler,
    TypeHandler,
    Dispatcher
)
import logging
from typing import List

from hidden_constants import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class Bot:
    def start(self, update: Update, context: CallbackContext) -> None:
        """Sends a message with 5 inline buttons attached."""
        update.message.reply_text(text="Choose an option:",
                                  reply_markup=self.build_keyboard())

    @staticmethod
    def build_keyboard() -> InlineKeyboardMarkup:
        buttons: List[InlineKeyboardButton] = [InlineKeyboardButton("Articles", callback_data="articles"),
                                               InlineKeyboardButton("Status", callback_data="status")]
        return InlineKeyboardMarkup.from_row(buttons)

    def status(self, update: Update, context: CallbackContext) -> None:
        # TODO
        # update.effective_user.send_message(Notifier.get_instance().get_status(), parse_mode=ParseMode.MARKDOWN_V2)
        raise NotImplementedError()

    def articles(self, update: Update, context: CallbackContext) -> None:
        # TODO
        raise NotImplementedError()

    def button_clicked(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        switcher = {
            "status": lambda: self.status(update, context),
            "articles": lambda: self.articles(update, context)
        }
        switcher.get(query.data)()

    def run(self) -> None:
        updater = Updater(
            BOT_TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.button_clicked))
        dispatcher.add_handler(CommandHandler("status", self.status))
        updater.start_polling()
        updater.idle()
