# © @JustRex ʀᴇxᴀ-ᴇx
# ⚠️ JANGAN HAPUS CREDIT ANJG!
# modification of the Cilik Userbot

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@Xa_cmd(pattern="sadvid$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@sadvideorexa", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Jangan Terlalu Sedih ya kak [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Maaf, kayaknya kamu ga pantes untuk sedih :) .")


CMD_HELP.update(
    {
        "sadvideo": f"**Plugin : **sadvideo\
        \n\n  ⌬  **Syntax :** {cmd}sadvid\
        \n  ⌬  **Function : **Untuk Mengirim video sad/sedih secara random.\
    "
    }
)
