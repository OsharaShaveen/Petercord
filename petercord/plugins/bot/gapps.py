"""Gapps via inline bot"""
import requests
from bs4 import BeautifulSoup
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from requests import get

from petercord import Config, Message, petercord

# TODO Make Check Admin and Sudos Wrapper


@petercord.on_cmd(
    "gapps", about={"header": "Get Android 10 arm64 GApps"}, allow_channels=False
)
async def gapps_inline(message: Message):
    await message.edit("`🔍 Finding Latest GApps...`")
    bot = await petercord.bot.get_me()
    x = await petercord.get_inline_bot_results(bot.username, "gapps")
    await petercord.send_inline_bot_result(
        chat_id=message.chat.id, query_id=x.query_id, result_id=x.results[0].id
    )
    await message.delete()


if petercord.has_bot:

    @petercord.bot.on_callback_query(filters.regex(pattern=r"^open_gapps$"))
    async def open_cb(_, callback_query: CallbackQuery):
        u_id = callback_query.from_user.id
        if u_id in Config.OWNER_ID or u_id in Config.SUDO_USERS:
            gapps_link = []
            r = requests.get(
                "https://raw.githubusercontent.com/Pharuxtan/OpenGappsFetcher/master/gapps.json"
            ).json()
            varient = [
                "aroma",
                "super",
                "stock",
                "full",
                "mini",
                "micro",
                "nano",
                "pico",
            ]
            try:
                for i in varient:
                    gapps_link.append(r["arm64"]["10.0"]["downloads"][i]["download"])
            except KeyError:
                return
            open_g = [
                [
                    InlineKeyboardButton(text="aroma", url=gapps_link[0]),
                    InlineKeyboardButton(text="super", url=gapps_link[1]),
                    InlineKeyboardButton(text="stock", url=gapps_link[2]),
                ],
                [
                    InlineKeyboardButton(text="full", url=gapps_link[3]),
                    InlineKeyboardButton(text="mini", url=gapps_link[4]),
                    InlineKeyboardButton(text="micro", url=gapps_link[5]),
                ],
                [
                    InlineKeyboardButton(text="nano", url=gapps_link[6]),
                    InlineKeyboardButton(text="pico", url=gapps_link[7]),
                ],
                [InlineKeyboardButton(text="⏪  BACK", callback_data="back_gapps")],
            ]

            await petercord.bot.edit_inline_text(
                callback_query.inline_message_id,
                "[\u200c](https://imgur.com/gallery/ieSTXbM) **OPEN GAPPS**",
                reply_markup=InlineKeyboardMarkup(open_g),
            )
        else:
            await callback_query.answer(
                "Sorry You Can't Access This!\n\n DEPLOY PETERCORD",
                show_alert=True,
            )

    @petercord.bot.on_callback_query(filters.regex(pattern=r"^flame_gapps$"))
    async def flame_cb(_, callback_query: CallbackQuery):
        u_id = callback_query.from_user.id
        if u_id in Config.OWNER_ID or u_id in Config.SUDO_USERS:
            link = "https://sourceforge.net/projects/flamegapps/files/arm64/android-10/"
            url = get(link)
            if url.status_code == 404:
                return
            page = BeautifulSoup(url.content, "lxml")
            content = page.tbody.tr
            date = content["title"]
            date2 = date.replace("-", "")
            flame = "{link}{date}/FlameGApps-10.0-{varient}-arm64-{date2}.zip/download"
            basic = flame.format(link=link, date=date, varient="basic", date2=date2)
            full = flame.format(link=link, date=date, varient="full", date2=date2)

            flame_g = [
                [
                    InlineKeyboardButton(text="FULL", url=full),
                    InlineKeyboardButton(text="BASIC", url=basic),
                ],
                [InlineKeyboardButton(text="⏪  BACK", callback_data="back_gapps")],
            ]

            await petercord.bot.edit_inline_text(
                callback_query.inline_message_id,
                "[\u200c](https://telegra.ph/file/6f3409899a5a6d7d4de78.jpg)**FLAME GAPPS**",
                reply_markup=InlineKeyboardMarkup(flame_g),
            )
        else:
            await callback_query.answer(
                "Sorry You Can't Access This!\n\n  DEPLOY PETERCORD",
                show_alert=True,
            )

    @petercord.bot.on_callback_query(filters.regex(pattern=r"^nik_gapps$"))
    async def nik_cb(_, callback_query: CallbackQuery):
        u_id = callback_query.from_user.id
        if u_id in Config.OWNER_ID or u_id in Config.SUDO_USERS:
            link = (
                "https://sourceforge.net/projects/nikgapps/files/Releases/NikGapps-Q/"
            )
            url = get(link)
            if url.status_code == 404:
                return
            page = BeautifulSoup(url.content, "lxml")
            content = page.tbody.tr
            date = content["title"]
            latest_niks = f"{link}{date}/"
            nik_g = [
                [InlineKeyboardButton(text="Lastest", url=latest_niks)],
                [InlineKeyboardButton(text="⏪  BACK", callback_data="back_gapps")],
            ]

            await petercord.bot.edit_inline_text(
                callback_query.inline_message_id,
                "[\u200c](https://imgur.com/gallery/ieSTXbM) **NIK GAPPS**",
                reply_markup=InlineKeyboardMarkup(nik_g),
            )
        else:
            await callback_query.answer(
                "Sorry You Can't Access This!\n\n DEPLOY PETERCORD",
                show_alert=True,
            )

    @petercord.bot.on_callback_query(filters.regex(pattern=r"^back_gapps$"))
    async def back_cb(_, callback_query: CallbackQuery):
        u_id = callback_query.from_user.id
        if u_id in Config.OWNER_ID or u_id in Config.SUDO_USERS:

            buttons = [
                [
                    InlineKeyboardButton("Open Gapps", callback_data="open_gapps"),
                    InlineKeyboardButton("Flame Gapps", callback_data="flame_gapps"),
                ],
                [InlineKeyboardButton("Nik Gapps", callback_data="nik_gapps")],
            ]

            await petercord.bot.edit_inline_text(
                callback_query.inline_message_id,
                "[\u200c](https://imgur.com/gallery/ieSTXbM) **LATEST Android 10 arm64 GApps**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        else:
            await callback_query.answer(
                "Sorry You Can't Access This!\n\n DEPLOY PETERCORD",
                show_alert=True,
            )
