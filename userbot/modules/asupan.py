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
                "@DESAHANFCE", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Nih kak desahannya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan desahan.")


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


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **asupan\
        \n\n  •  **Syntax :** {cmd}asupan\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** {cmd}desah\
        \n  •  **Function : **Untuk Mengirim voice desah secara random.\
        \n\n  •  **Syntax :** {cmd}vidlucu\
        \n  •  **Function : **Untuk Mengirim video lucu secara random.\
"
    }
)
