# Made by @JustRex
# Kalo mau kopas izin lah paling engga


import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@Xa_cmd(pattern="alquran$")
async def _(event):
    try:
        alqurannya = [
            alquran
            async for alquran in event.client.iter_messages(
                "@alquranxauserbot", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(alqurannya),
            caption=f"nih kak suratnya, semoga berkah buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Maaf, lagi ga ada suratnya .")


@Xa_cmd(pattern="sholawat$")
async def _(event):
    try:
        sholawatnya = [
            sholawat
            async for sholawat in event.client.iter_messages(
                "@sholawatxauserbot", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(sholawatnya),
            caption=f"nih kak sholawatnya, semoga berkah buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Maaf, lagi ga ada suratnya .")


@Xa_cmd(pattern="seger$")
async def _(event):
    try:
        segernya = [
            seger
            async for seger in event.client.iter_messages(
                "@intinyabikinseger", filter=InputMessagesFilterPhoto
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(segernya),
            caption=f"Masa iya sih [{owner}](tg://user?id={aing.id}) kehasut puasanya?",
        )
        await event.delete()
    except Exception:
        await event.edit("lagi ga ada setan Alhamdulillah .")


CMD_HELP.update(
    {
        "ramadhan2": f"**Plugin : **ramadhan2\
        \n\n  ⌬  **Perintah :** {cmd}alquran\
        \n  ⌬  **Function : **Untuk mengirim surat Al-Quran\
        \n\n  ⌬  **Perintah :** {cmd}sholawat\
        \n  ⌬  **Function : **Untuk Sholawat Sholawat\
        \n\n  ⌬  **Perintah :** {cmd}seger\
        \n  ⌬  **Function : **ketik ini Ketika siang hari panas.\
    "
    }
)
