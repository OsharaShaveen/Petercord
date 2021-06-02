
import asyncio
from collections import deque

from petercord import Message, petercord

from petercord import Config, ALIVE_LOGO


@petercord.on_cmd("simboll$", about={"header": "alive"})
async def alive_(message: Message):
    """alive"""
    animation_interval = 0.0
    animation_ttl = range(117)
    await message.edit(
    "**▬▬▬▬▬▬❙۩🛡🛡۩❙▬▬▬▬▬▬**\n"
     " **🔮 PETERCORD-USERBOT 🔮** \n\n"
     "🛡 **PETERCORD**     \n   ➥ `USERBOT TELEGRAM` \n"
     "🛡 **Username** \n   ➥ `@{user.username}` \n"
     "🛡 **Telethon** \n   ➥ `Versi VXL.2021` \n"
     "🛡 **Python**   \n   ➥ `Versi {python_version()}` \n"
     "🛡 **Versi Bot**\n   ➥ `PETERCORD ILHAM MANSIEZ` \n"
     "🛡 **Modul**    \n   ➥ `PLUGINS` \n\n"
     "🛡 **Repo Userbot:** [PETERCORD](https://github.com/IlhamMansiez/PETERCORD)\n🛡 **Grup Userbot: **[Tekan](https://t.me/TEAMSquadUserbotSupport)\n🛡 **Pemilik:** [IlhamMansiez](t.me/diemmmmmmmmmm)\n"
     "**▬▬▬▬▬▬❙۩🛡🛡۩❙▬▬▬▬▬▬**")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await message.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(200)
            await msg.delete()
        except BaseException:
            await message.edit(
                output + "\n\n *`The provided logo is invalid."
                "\nMake sure the link is directed to the logo picture`"
            )
            await asyncio.sleep(100)
            await message.delete()
    else:
        await message.edit(output)
        await asyncio.sleep(100)
        await message.edit(text=out, del_in=3)
