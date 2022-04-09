# © @tofik_dn
# ⚠️ Do not remove credits
# recode by @greyyvbss
# video lucu & sad by @JustRex

import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@Xa_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@asupancilikbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Nih kak asupan buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@Xa_cmd(pattern="desah$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@deshanhiroshi", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Jangan Sange ya kak, nih desah buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("sange nya ditahan dulu ya kak.")


@Xa_cmd(pattern="vidlucu$")
async def _(event):
    try:
        vidlucunya = [
            vidlucu
            async for vidlucu in event.client.iter_messages(
                "@videolucuxauserbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(vidlucunya),
            caption=f"Nih kak video lucunya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video lucu.")


@Xa_cmd(pattern="ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Ayang nya** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA CAKEP!.**")


@Xa_cmd(pattern="vidsad$")
async def _(event):
    try:
        sadvidnya = [
            sadvid
            async for sadvid in event.client.iter_messages(
                "@sadvideorexa", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(sadvidnya),
            caption=f"Jangan Terlalu Sedih ya kak [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Maaf, kayaknya kamu ga pantes untuk sedih :) .")


@Xa_cmd(pattern="asupan2$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Okeokelhh", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Nih kak asupan buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@Xa_cmd(pattern="kpop$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@pictsenadaidol", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Nih Foto Kpop buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Fotonya coba lagi ya.")


@Xa_cmd(pattern="ttfyp$")
async def _(event):
    try:
        fypnya = [
            fyp
            async for fyp in event.client.iter_messages(
                "@cah0192837465", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(fypnya),
            caption=f"Tiktok Random Video by [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video, maaf coba lagi.")


@Xa_cmd(pattern="nc$")
async def _(event):
    try:
        bokepnya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@sangeyaaaaaa", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(bokepnya),
            caption=f"**negative content by** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan, tahsn dulu sangenya.**")



CMD_HELP.update(
    {
        "asupan": f"**Plugin : **asupan\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}asupan\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}asupan2\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video asupan Cewe.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}desah\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim voice desah secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vidlucu\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video lucu secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ayang\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendapatkan Ayang mu, hehe.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vidsad\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video sad random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}kpop\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat foto idol kpop random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ttfyp\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video dari tiktok secara random.\
"
    }
)
