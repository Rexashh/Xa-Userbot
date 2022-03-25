# © @tofik_dn
# ⚠️ Do not remove credits
# recode by @greyyvbss
# video lucu by @JustRex

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice


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
            caption=f"Nih kak asupannya [{owner}](tg://user?id={aing.id})",
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
                "@videolucuxauserbot", filter=InputMessagesFilterVoice
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
                "@IndomieGantengV2", filter=InputMessagesFilterPhotos
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Ayang nya** [{aku.first_name}](tg://user?id={aku.id})")

        await event.delete()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA CAKEP!.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **asupan\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}asupan\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}desah\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim voice desah secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vidlucu\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video lucu secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ayang\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendapatkan Ayang mu, hehe.\
"
    }
)
