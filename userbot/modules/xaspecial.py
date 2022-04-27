# xa-userbot special
# jangan hapus credit memek!

import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterPhotos


@Xa_cmd(pattern="vl$")
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


@Xa_cmd(pattern="vs$")
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
                "@fakyudurov", filter=InputMessagesFilterVideo
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


@Xa_cmd(pattern="ppcp$")
async def _(event):
    try:
        ppcpnya = [
            ppcp
            async for ppcp in event.client.iter_messages(
                "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        xa = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ppcpnya),
            caption=f"pp couple by [{owner}](tg://user?id={xa.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


@Xa_cmd(pattern="memeid$")
async def _(event):
    try:
        memexanya = [
            memexa
            async for memexa in event.client.iter_messages(
                "@meme_comic", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(memexanya),
            caption=f"meme by[{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


CMD_HELP.update(
    {
        "xaspecial": f"**Plugin : **xaspecial\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vl\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video lucu secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ayang\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendapatkan Ayang mu, hehe.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vs\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video sedih secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}kpop\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat foto idol kpop random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ttfyp\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video dari tiktok secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ppcp\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendapatkan pp couple secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}memeid\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendspatkan foto meme secara random.\
"
    }
)
