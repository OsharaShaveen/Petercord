# petercord

from petercord import petercord, Message, Config, versions


@petercord.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
   Petercord-X\n
• **VERSION** : `3.03`
• **REPO** : [Click here]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
