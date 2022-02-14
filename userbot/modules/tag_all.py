# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""A Plugin to tagall in the chat for @UniBorg and cmd is `.all`"""


from userbot import CMD_HELP, bot
from userbot.events import rose_cmd
from userbot import CMD_HANDLER as cmd


@bot.on(rose_cmd(outgoing=True, pattern=r"all(?: |$)(.*)"))
async def all(event):
    if event.fwd_from:
        return
    await event.delete()
    mentions = "@all"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 200000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)


CMD_HELP.update({
    "tagall":
    f"✘ **Plugin tagall** :\
\n\n  •  **Perintah** : `{cmd}all` \
  \n  •  **Fungsi** : Untuk Mengetag semua anggota yang ada di group."})
