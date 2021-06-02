# petercord

from petercord import petercord, Message, Config, versions


@petercord.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
**HI**, __WELCOME PETERCORD USERBOT__ 🎖 **PETERCORD** 🎖
    __DATA PETERCORD__
• **PETERCORD VERSION** : `⚡2021-ILHAM-MANSIEZ⚡`
• **LICENSE** : {versions.__license__}
• **COPYRIGHT** : {versions.__copyright__}
• **REPO** : [PETERCORD]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
