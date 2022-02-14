""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.events import rose_cmd
from userbot import CMD_HANDLER as cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(rose_cmd(outgoing=True, pattern=r"rhelp(?: |$)(.*)"))
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/JustRex)"
        "\n[Repo](https://github.com/Rexashh/Xa-UserBot)"
        "\n[Instagram](instagram.com/syhndr_)")


@bot.on(rose_cmd(outgoing=True, pattern=r"vars(?: |$)(.*)"))
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/SendiAp/Rose-Userbot/Rose-Userbot/varshelper.txt)")



CMD_HELP.update({
    "helper":
    f"✘ Plugin helper :\
\n\n  •  Perintah : `{cmd}vars` \
  \n  •  Fungsi : Melihat Daftar Vars.\
\n\n  •  Perintah : `{cmd}rhelp` \
  \n  •  Fungsi : Bantuan Untuk Xa-Userbot."})
