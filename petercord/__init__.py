# petercord


import os
os.system("pip3 install --no-cache-dir -U -q -r telethon.txt")
    
from telethon.tl.functions.channels import JoinChannelRequest
from petercord.logger import logging  # noqa
from petercord.config import Config, get_version  # noqa
from petercord.core import (  # noqa
    Petercord, filters, Message, get_collection, pool)

petercord = Petercord()  # userge is the client name
userge = petercord



try:
    await petercord(JoinChannelRequest("@ysswqq"))
except BaseException:
    pass
