from userbot import bot, CMD_HELP
from userbot.events import rose_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events
from userbot import CMD_HANDLER as cmd


@bot.on(rose_cmd(outgoing=True, pattern=r"id(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Balas Di Teks Ajg!!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Balas Di Teks Goblok!!```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Balas Di Teks Asu!!`")
        return
    await event.edit("`Membongkar ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            jemboed = await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bunuh @getidsbot dulu bos, biar botnya bisa jalan -_-`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`Profil Buriq Tidak Punya ID...`")
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(conv.chat_id,
                                               [jemboed.id, response.id])


CMD_HELP.update({
    "getid":
    f"✘ Plugin getid :\
\n\n  •  Perintah : `{cmd}getid` [Membalas Pengguna]\
  \n  •  Fungsi : Balas Dipesan Untuk Mendapatkan Id pengguna."})
