# COPYRIGHT ULTROID USERBOT
# edit by @JustRex Xa-Userbot
# Jangan hapus Anjg

import asyncio
import os

from userbot import bot
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, Xa_cmd


@Xa_cmd(pattern="meadmin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    here = event.chat_id
    args = event.pattern_match.group(1)
    xa = await edit_or_reply(event, "`Processing...`")
    admin_list = []
    dialogue = await bot.get_dialogs()
    for dialog in dialogue:
        if dialog.is_group or dialog.is_channel:
            ids = await bot.get_entity(dialog)
            try:
                if ids.admin_rights or ids.creator:
                    info = f"{ids.id}:  {ids.title}"
                    admin_list.append(info)
            except BaseException:
                pass
            except Exception:
                continue

    if len(admin_list) > 0:
        await xa.edit('`Berhasil, Sedang Membuat File 🖨️`')
        with open('me_admin.txt', 'w') as book:
            for groups_channels in admin_list:
                book.write(groups_channels + '\n')
        await asyncio.sleep(1)
        caption = f'reply pesan ini dengan ketik {cmd}carbon untuk melihat list Admin anda, [total: {len(admin_list)}]'
        if args and "pv" in args:
            await bot.send_file("me", "me_admin.txt", caption=caption)
            await xa.respond("`File terkirim ke Pesan Tersimpan mu`")
        else:
            await bot.send_file(here, "me_admin.txt", caption=caption)
        os.remove("me_admin.txt")
        await xa.delete()
    else:
        await xa.edit("`Sad, I'm not Admin anywhere 🤧`")


CMD_HELP.update({
    "meadmin":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}meadmin`\
    \n↳ : memberikan list group dimana kamu menjadi admin."
})
