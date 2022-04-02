# @JustRex
# Xa-Userbot
# Special Ramadhan

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, Xa_cmd


@Xa_cmd(pattern="sholat2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**LU NGAPAIN PUASA KALO GA SHOLAT TOLOL?BATALAIN AJA GOBLOK!**")


@Xa_cmd(pattern="bukber5(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**kemarin ada yang ngajak gua bukber, tapi Cuma wacana, Kalo tau gitu ga usah ajak ajak gua bukber ye anj!**")


@Xa_cmd(pattern="setan4(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**TAU GA LU?**")
    sleep(1.5)
    await edit_or_reply(event, "**Lo itu SETAN yang Lolos waktu pintu NERAKA ditutup!**")


@Xa_cmd(pattern="taraw3(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**TARAWEH BEGO BUKAN MAIN TELE! KIBLAT LU TELEGRAM EMANG?**")


@Xa_cmd(pattern="taraw4(?:|$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Malu napa bego, yang lain pada taraweh lo kagak! gua sih malu**")


@Xa_cmd(pattern="mp(?:|$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Setidaknya KALO GA PUASA MALU NAPA GOBLOK JANGAN DIUMBAR UMBAR, KESANNYA NORAK!**")


@Xa_cmd(pattern="pk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BUAT COWO YANG GAK PUASA, POTONG AJA KONTOLNYA!!**")


@Xa_cmd(pattern="aus1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**LAGI WUDHU GA SENGAJA KEMINUM, YAUDAH GUA LANJUTIN MINUM AIR KULKAS**")


@Xa_cmd(pattern="aus2(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BELI ES CEKEK ENAK BGT INI ASLI DAH **")


@Xa_cmd(pattern="tox1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Lagi ga pengen toxic soalnya puasa**")


@Xa_cmd(pattern="setan5(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**GUA GA GAMPANG KEHASUT SETAN KEK LU YA !**")


@Xa_cmd(pattern="kolek1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BAGI KOLEK LAH!!!!**")


@Xa_cmd(pattern="sebat1(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BENTAR....**")
    sleep(1.5)
    await edit_or_reply(event, "**GUA SEBAT DULU ABIS ITU LANJUT PUASA**")


@Xa_cmd(pattern="sah(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**SAHUR DOANG PUASA KAGAK!!!!**")


@Xa_cmd(pattern="mamadede(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**NOBAR MAMA DEDE SKUY!!!**")


@Xa_cmd(pattern="warp(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**WAR WER WOR! PUASA TOLOL!**")


CMD_HELP.update(
    {
        "ramadhan2": f"**Plugin : **`ramadhan3`\
        \n\n    **Perintah :** `{cmd}sholat2`\
        \n⌬    **Fungsi : **ngatain orang yang puasa tapi ga sholat.\
        \n\n    **Perintah :** `{cmd}bukber5`\
        \n⌬    **Fungsi : **Cobain aja lah anjg.\
        \n\n    **Perintah :** `{cmd}setan4`\
        \n⌬    **Fungsi : **ngatain orang setan.\
        \n\n    **Perintah :** `{cmd}setan5`\
        \n⌬    **Fungsi : **Ini buat lu hehe.\
        \n\n    **Perintah :** `{cmd}taraw4`\
        \n⌬    **Fungsi : **taraweh, intinya cobain aja.\
        \n\n    **Perintah :** `{cmd}mp`\
        \n⌬    **Fungsi : **malu gblk klo ga puasa?.\
        \n\n    **Perintah :** `{cmd}pk`\
        \n⌬    **Fungsi : **Potong aja kontolnya.\
        \n\n    **Perintah :** `{cmd}aus1`\
        \n⌬    **Fungsi : **cobain aja.\
        \n\n    **Perintah :** `{cmd}aus2`\
        \n⌬    **Fungsi : **ini kalo misalnya lu aus.\
        \n\n    **Perintah :** `{cmd}tox1`\
        \n⌬    **Fungsi : **toxic dikit hehe.\
        \n\n    **Perintah :** `{cmd}kolek`\
        \n⌬     **Fungsi: **minta kolek.\
        \n\n    **Perintah :** `{cmd}sebat1`\
        \n⌬    **Fungsi : **sebat dikit.\
        \n\n    **Perintah :** `{cmd}sah`\
        \n⌬    **Fungsi : **cobain aja.\
        \n\n    **Perintah:** `{cmd}mamadede`\
        \n⌬    **Fungsi: **nobar mama dede.\
        \n\n    **Perintah:** `{cmd}warp`\
        \n⌬    **Fungsi: **ngatain war."
    })
