# Port By @VckyouuBitch From Geez - Project
# Copyright © Geez - Project
# Credits By Ultroid

from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name

from userbot import CMD_HANDLER as cmd
from userbot.events import rose_cmd
from userbot import CMD_HELP, bot


@bot.on(rose_cmd(pattern="tag(on|off|all|bots|rec|admins|owner)?(.*)", outgoing=True))
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if lll:
        xx = f"{lll}"
    else:
        xx = ""
    async for bb in e.client.iter_participants(e.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                xx += f"\n👑 [{get_display_name(bb)}](tg://user?id={bb.id}) 👑"
        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "bot" in okk:
            if bb.bot:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
    await e.client.send_message(e.chat_id, xx)
    await e.delete()


CMD_HELP.update({
    "tags":
    f"**✘ Plugin** `tags` :\
\n\n  •  **Perintah :** `{cmd}tag all`\
  \n  •  **Fungsi : **Tag Top 100 Members of chat.\
\n\n  •  **Perintah :** `{cmd} tag admin` \
  \n  •  **Fungsi : **Tag Admins of that chat.\
\n\n  •  **Perintah :** `{cmd}tag owner` \
  \n  •  **Fungsi : **Tag Owner of that chat.\
\n\n  •  **Perintah :** `{cmd}tag bot` \
  \n  • ** Fungsi: **Tag Bots of that chat.\
\n\n  •  **Perintah :** `{cmd}tag rec`\
  \n  •  **Fungsi : **Tag recently Active Members.\
\n\n  • ** Perintah: ** `{cmd}tag on` \
  \n  • ** Fungsi: **Tag online Members(work only if privacy off).\
\n\n  • ** Perintah: ** `{cmd}tag of`\
  \n  • ** Fungsi: **Tag offline Members(work only if privacy off)."})
