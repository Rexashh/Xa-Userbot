# Jangan hapus ini ya mmk!
# By @JustRex Xa-Userbot

from time import sleep

import random

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import Xa_cmd

from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos



@Xa_cmd(pattern=r"lebaran2(?: |$)(.*)")
async def _(typew):
    await typew.edit("🕌")
    await typew.edit("🕌🕌")
    await typew.edit("🕌🕌🕌")
    awiat typew.edit("✨")
    sleep(1)
    await typew.edit("🕌 𝙎𝙚𝙡𝙖𝙢𝙖𝙩 𝙃𝙖𝙧𝙞 𝙍𝙖𝙮𝙖 𝙄𝙙𝙪𝙡 𝙁𝙞𝙩𝙧𝙞 🕌\n"
                     " Ramadhan akan segera pergi, tapi diri tak bisa suci\n"
                     " Jika marah dan sakit hati belum juga bisa dimaafkan dan dimengerti\n"
                     " Taqobballahu minna wa minkum \n"
                     " Taqobbal ya Kariim\n"
                     " Mohon maaf lahir dan batin\n")
                     
                     
@Xa_cmd(pattern=r"lebaran3(?: |$)(.*)")
async def _(typew):
    await typew.edit("𝐌𝐢𝐧𝐚𝐥 '𝐀𝐢𝐝𝐢𝐧 𝐰𝐚𝐥-𝐅𝐚𝐢𝐳𝐢𝐧🕌\n"
                                     "mohon maaf kalo ada salah kata,\n"
                                     "salah cinta, atau salah menaruh rasa\n"
                                     "Selamat  Hari Raya Idul Fitri 🕌\n")

@Xa_cmd(pattern=r"lebaran4(?: |$)(.*)")
async def _(typew):
    await typew.edit("CTRL + S berkah Ramadan\n"
                                     "CTRL + A, DEL Dosa dan kesalahan\n"
                                     "CTRL + C, CTRL + V Kebahagian Lebaran\n"
                                     "Selamat Idul Fitri teman-teman\n")
 
@Xa_cmd(pattern=r"lebaran5(?: |$)(.*)")
async def _(typew):
    await typew.edit("Walaupun gua pernah nyimpen perasaan ke lu, setidaknya gua ga mau nyimpen dosa ke lu,")
    sleep(1)
    await typew.edit("Jadiii... ")
    sleep(1)
    await typew.edit("Maaf kalo gua pernah suka & cinta sama lu ")
    sleep(0.5)   
    await typew.edit("Eh maksudnya, pernah berbuat salah ke lu ")  
    sleep(1) 
    await typew.edit("maafin ya!!")                

@Xa_cmd(pattern="lebaran6$")
async def _(event):
    try:
        lebarannya = [
            lebaran
            async for lebaran in event.client.iter_messages(
                "@lebaranxauserbot", filter=InputMessagesFilterPhotos
            )
        ]
        xa = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(lebarannya),
            caption=f" saya [{owner}](tg://user?id={xa.id}) dan sekeluarga mengucapkan ",
                             f" Mengucapkan Minal 'Aidin wal-Faizin",
                             f" Mohon Maaf Lahir dan Batin",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


@Xa_cmd(pattern=r"petasan(?: |$)(.*)")
async def _(typew):
    await typew.edit("🎆")
    sleep(2)
    await typew.edit("🎆")
    sleep(2)
    await typew.edit("𝐒𝐄𝐋𝐀𝐌𝐀𝐓 𝐈𝐃𝐔𝐋 𝐅𝐈𝐓𝐑𝐈 1443")
    sleep(1)
    await typew.edit("Mohon Maaf Lahir Dan Batin")
    
    
@Xa_cmd(pattern=r"thr(?: |$)(.*)")
async def _(typew):
    await typew.edit("Sory, lebih butuh Thr daripada Maaf dari lu !")
    
@Xa_cmd(pattern=r"slok(?: |$)(.*)")
async def _(typew):
    await typew.edit("Udah Kelar nih Puasanya, Mau berantem ga? Sharelok cepet!")
    
@Xa_cmd(pattern=r"thr2(?: |$)(.*)")
async def _(typew):
    await typew.edit("Minal aidzin Bro! Jangan lupa kirim thr ke rekening gua")  
    

@Xa_cmd(pattern=r"thr3(?: |$)(.*)")
async def _(typew):
    await typew.edit("Lebaran nih...")
    sleep(1)
    await typew.edit("Bagi Thr lah jjingg!!!!")
    
    
        
CMD_HELP.update(
    {
        "idulfitri": f"**Plugin : **`idulfitri`\
        \n\n  •  **Perintah :** `{cmd}lebaran1`\
        \n  🕌  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran2`\
        \n  🕌  **Fungsi : **Coba Aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran3`\
        \n  🕌  **Fungsi : **Coba Aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran4`\
        \n  🕌  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran5`\
        \n  🕌  **Fungsi : **Coba aja.\
        \n\n  •  **Perintah :** `{cmd}lebaran6`\
        \n  🕌  **Fungsi : **Coba aja.\     
        \n\n  •  **Perintah :** `{cmd}petasan`\
        \n  🕌  **Fungsi : **Coba aja.\   
        \n\n  •  **Perintah :** `{cmd}thr`\
        \n  🕌  **Fungsi : **Coba aja.\      
        \n\n  •  **Perintah :** `{cmd}slok`\
        \n  🕌  **Fungsi : **Coba aja.\  
        \n\n  •  **Perintah :** `{cmd}thr2`\
        \n  🕌  **Fungsi : **Coba aja.\        
        \n\n  •  **Perintah :** `{cmd}thr3`\
        \n  🕌  **Fungsi : **Coba aja.\                
    "
    }
)
