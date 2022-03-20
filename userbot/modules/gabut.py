from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import Xa_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@Xa_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@Xa_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@Xa_cmd(pattern="naon(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`naon sih sia ?`")
# naon


@Xa_cmd(pattern="perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


@Xa_cmd(pattern="ox(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gua Rexa Aditya`")
    sleep(2)
    await event.edit(f"`Gua Tinggal Di Kota Paling Panas Katanya sih`")
    sleep(2)
    await event.edit(f"`Tau Kota Bekashit kan?`")
    sleep(2)
    await event.edit(f"`Nah disitu gua tinggal`")
    sleep(2)
    await event.edit(f"`Anu`")
    sleep(1.5)
    await event.edit(f"`Umur gua`")
    sleep(2)
    await event.edit(f"`20 tahun, ga tua ga muda kan hehe`")
    sleep(2)
    await event.edit(f"`Hobi gua apa ya`")
    sleep(2)
    await event.edit(f"`hmmmm`")
    sleep(1)
    await event.edit(f"`Selain Mageran`")
    sleep(2)
    await event.edit(f"`Gua Suka baca novel`")
    sleep(2)
    await event.edit(f"`Nonton Anime`")
    sleep(2)
    await event.edit(f"`Drakor`")
    sleep(1.5)
    await event.edit(f"`Western`")
    sleep(1.5)
    await event.edit(f"`banyak pokoknya`")
    sleep(1.5)
    await event.edit(f"`termasuk bokep`")
    sleep(2)
    await event.edit(f"`genre musik ku`")
    sleep(2)
    await event.edit(f"`hmmmm`")
    sleep(1.5)
    await event.edit(f"`yang paling fav sih POP PUNK`")
    sleep(2)
    await event.edit(f"`Udah gitu aja wkwk`")
    sleep(2)
    await event.edit(f"`Terakhir deh`")
    sleep(2)
    await event.edit(f"`Gua addict sama boba`")
    sleep(2)
    await event.edit(f"`Dahhh Makasih, babayyy`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
# Perkenalan rexa


CMD_HELP.update({
    "gabut": f"**Modules** - `Gabut`\
    \n\n Cmd : `{cmd}l`\
    \nUsage : Untuk Menjawab Salam\
    \n\n Cmd : `{cmd}perkenalan`\
    \nUsage : Memperkenalkan Diri\
    \n\n Cmd : `{cmd}p`\
    \nUsage : Untuk Memberi Salam."
    \n\n Cmd: `{cmd}naon`
    \nUsage: coba aja sendiri
    \n\n Cmd: `{cmd}ox`
    \nUsage: Perkenalan Owner Xa - Userbot
})
