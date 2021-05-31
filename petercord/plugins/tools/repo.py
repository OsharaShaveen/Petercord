# petercord

from petercord import Config, Message, petercord


@petercord.on_cmd("repo", about={"header": "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"• **repo** : [PETERCORD]({Config.UPSTREAM_REPO})"
    await message.edit(output)
