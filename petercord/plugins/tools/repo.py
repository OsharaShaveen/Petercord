# petercord

from petercord import petercord, Message, Config, versions


@petercord.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
   Petercord-X
• **VERSION** : `3.03`
• **LICENSE** : {versions.__license__}
• **COPYRIGHT** : {versions.__copyright__}
• **REPO** : [Click here]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
