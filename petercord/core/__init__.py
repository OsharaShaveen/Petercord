# petercord
import os
os.system("pip3 install --no-cache-dir -U -q -r telethon.txt")
    

from pyrogram import filters  # noqa

from .database import get_collection  # noqa
from .ext import pool  # noqa
from .types.bound import Message  # noqa
from .client import Petercord  # noqa
