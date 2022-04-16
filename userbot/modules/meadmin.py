import asyncio
import os

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, Xa_cmd


@Xa_cmd(pattern="meadmin ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    here = event.chat_id
    args = event.pattern_match.group(1)
    e1 = await eor(event, "`Processing...`")
    admin_list = []
    dialogue = await ultroid_bot.get_dialogs()
    for dialog in dialogue:
        if dialog.is_group or dialog.is_channel:
            ids = await ultroid_bot.get_entity(dialog)
            try:
                if ids.admin_rights or ids.creator:
                    info = f"{ids.id}:  {ids.title}"
                    admin_list.append(info)
            except BaseException:
                pass
            except Exception:
                continue

    if len(admin_list) > 0:
        await e1.edit('`Berhasil, Sedang Membuat File 🖨️`')
        with open('me_admin.txt', 'w') as book:
            for groups_channels in admin_list:
                book.write(groups_channels + '\n')
        await asyncio.sleep(1)
        caption = f'List of Chats Where I have Admin Rights [total: {len(admin_list)}]'
        if args and "pv" in args:
            await ultroid_bot.send_file("me", "me_admin.txt", caption=caption)
            await e1.respond("`File terkirim ke Pesan Tersimpan mu`")
        else:
            await ultroid_bot.send_file(here, "me_admin.txt", caption=caption)
        os.remove("me_admin.txt")
        await e1.delete()
    else:
        await e1.edit("`Sed, I'm not Admin anywhere 🤧`")
        
        
        
CMD_HELP.update({"meadmin": f"\n\n𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝: `{cmd}meadmin`
                 "\n⌬ Memberikan list group dimana kamu menjadi admin."})
