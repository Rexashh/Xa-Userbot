# © @JustRex
# Jangan hapus Credit!

import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVoice


@Xa_cmd(pattern="seg$")
async def _(event):
    try:
        segernya = [
            seger
            async for seger in event.client.iter_messages(
                "@intinyabikinseger", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(segernya),
            caption=f"Nih Buat [{owner}](tg://user?id={aing.id}) Lumayan siang siang hehe.",
        )
        await event.delete()
    except Exception:
        await event.edit("Setannya lagi ga ada.")
        
        
@Xa_cmd(pattern="alquran$")
async def _(event):
    try:
        alqurannya = [
            alquran
            async for alquran in event.client.iter_messages(
                "@tobatxa", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(alqurannya),
            caption=f"Nih Buat [{owner}](tg://user?id={aing.id}) semoga berkah ya kak.",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan surat al-quran.")


CMD_HELP.update(
    {
        "ramadhan3": f"**Plugin : **ramadhan3\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}seg\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Buat panas panasin wkwkwk.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}alquran\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Mengirim ayat ayat Al-Qur'an.\       
"
    }
)
 
