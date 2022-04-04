# JANGAN HAPUS INI! © @JustRex
# Copyright Milik Xa-Userbot


import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos


@Xa_cmd(pattern="ppanime$")
async def _(event):
    try:
        ppanimenya = [
            ppanime
            async for ppanime in event.client.iter_messages(
                "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ppanimenya),
            caption=f"**nih pp anime buat** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Lagi Ga Nemu pp anime!.**")


@Xa_cmd(pattern="wallanime$")
async def _(event):
    try:
        wallpapernya = [
            wallpaper
            async for wallpaper in event.client.iter_messages(
                "@Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(wallpapernya),
            caption=f"**Anime Wallpaper By** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**Silahkan coba lagi.**")


@Xa_cmd(pattern="shortanime$")
async def _(event):
    try:
        shortanimenya = [
            shortanime
            async for shortanime in event.client.iter_messages(
                "@anime_status998", filter=InputMessagesFilterVideos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(shortanimenya),
            caption=f"**short anime video by** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**maaf lagi ga ada videonya, coba lagi deh.**")


CMD_HELP.update({
    "wibu2": f"𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝: `{cmd}ppanime`\
    \n↳ : untuk mendapatkan pp anime random.\
    \n\n𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝: `{cmd}wallanime`\
    \n↳ : Untuk Mendapatkan Wallpaper Aninme Random.\
    \n\n𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝: `{cmd}shortanime`\
    \n↳ : Untuk Mendapatkan Video Anime Pendek untuk Status whatsapp."
})
