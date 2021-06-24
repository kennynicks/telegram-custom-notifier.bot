from __future__ import annotations

import logging
import os

from telegram import ParseMode
from telegram.ext import (
    Updater
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


class Bot:
    def __init__(self) -> None:
        self.updater = Updater(os.getenv("BOT_TOKEN"))

    def send_message(self, chat_message: str) -> None:
        self.updater.bot.sendMessage(os.getenv("CHAT_ID"), chat_message, parse_mode=ParseMode.MARKDOWN_V2)

    def run(self) -> None:
        self.updater.start_polling()
        self.updater.idle()
