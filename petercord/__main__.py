# petercord

from petercord import petercord
CHANNEL = petercord.getCLogger(__name__)
from .config import get_version

ON = f"""
👥 **Petercord-X Aktif**
•••••••••••
💻 **Version -** `{get_version()}`

❗Sebaiknya Anda jangan keluar grup ini agar bot tidak mati
 ....Terimakasih....🇮🇩
❗You should not leave this group so that the bot does not die
 ....Thank You....🇺🇸
•••••••••••
"""

if __name__ == "__main__":
    await CHANNEL.log(ON)
    petercord.begin()
