import json

import aiohttp

from petercord import Config, Message, petercord
from petercord.utils.functions import get_emoji_regex

CHANNEL = petercord.getCLogger(__name__)
LOG = petercord.getLogger(__name__)


@petercord.on_cmd(
    "cr",
    about={
        "header": "use this to convert currency & get exchange rate",
        "description": "Convert currency & get exchange rates.",
        "examples": "{tr}cr 1 BTC USD",
    },
)
async def cur_conv(message: Message):
    """
    this function can get exchange rate results
    """
    if Config.CURRENCY_API is None:
        await message.edit(
            "<code>Oops!!get the API from</code> "
            "<a href='https://free.currencyconverterapi.com'>HERE</a> "
            "<code>& add it to Heroku config vars</code> (<code>CURRENCY_API</code>)",
            disable_web_page_preview=True,
            parse_mode="html",
            del_in=0,
        )
        return

    filterinput = get_emoji_regex().sub("", message.input_str)
    curcon = filterinput.upper().split()

    if len(curcon) == 3:
        amount, currency_to, currency_from = curcon
    else:
        await message.edit("`something went wrong!! do .help cr`")
        return

    if amount.isdigit():
        async with aiohttp.ClientSession() as ses:
            async with ses.get(
                "https://free.currconv.com/api/v7/convert?"
                f"apiKey={Config.CURRENCY_API}&q="
                f"{currency_from}_{currency_to}&compact=ultra"
            ) as res:
                data = json.loads(await res.text())
        try:
            result = data[f"{currency_from}_{currency_to}"]
        except KeyError:
            LOG.info(data)
            await message.err("invalid response from api !")
            return
        result = float(amount) / float(result)
        result = round(result, 5)
        await message.edit(
            "**CURRENCY EXCHANGE RATE RESULT:**\n\n"
            f"`{amount}` **{currency_to}** = `{result}` **{currency_from}**"
        )
        await CHANNEL.log("`cr` command executed sucessfully")

    else:
        await message.edit(
            r"`This seems to be some alien currency, which I can't convert right now.. (⊙_⊙;)`",
            del_in=0,
        )
