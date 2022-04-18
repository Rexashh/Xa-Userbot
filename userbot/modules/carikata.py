# " Made by @e3ris for Ultroid. "
# < https://github.com/TeamUltroid/Ultroid >
# idea: https://t.me/TelethonChat/256160
# recode by @JustRex


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, Xa_cmd


@Xa_cmd(pattern="cari( -r|) ?(.*)")
async def searcher(e):
    rex = await edit_or_reply(e, "`Mencari Pesan..`")
    args = e.pattern_match.group(2)
    limit = 5
    if not args or len(args) < 2:
        await edit_or_delete(rex, "Invalid argument!, Coba Lagi")
        return

    if ":" in args:
        args, limit = args.split(":", 1)
    try:
        limit = int(limit)
    except BaseException:
        limit = 5

    limit = 99 if limit > 99 else limit
    text, c = "", 0
    async for msg in e.client.iter_messages(
        e.chat_id,
        search=args.strip(),
        limit=limit,
        reverse=bool(e.pattern_match.group(1)),
    ):
        text += f" [»» {msg.id}](t.me/c/{e.chat.id}/{msg.id})\n"
        c += 1

    txt = (
        f"**Hasil Pencarian Kata :**  `{args}` \n\n{text}"
        if c > 0
        else f"**Tidak ada Hasil Pencarian Kata :**  `{args}`"
    )
    await rex.edit(txt)

CMD_HELP.update(
    {
        "carikata": f"**Plugin : **carikata\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}cari\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **kamu bisa mencari kata digroup, contoh {cmd}cari Heroku.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}cari -r\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk mencari kata dengan jumlah, contoh {cmd}cari -r heroku : 10.\
"
    }
)
