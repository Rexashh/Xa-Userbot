# © @JustRex Xa-Userbot
# I took these modules from ultroid and modified them
# Jangan hapus yg ada tanda # kontol!

from userbot.utils import Xa_cmd
import asyncio


@Xa_cmd(pattern="lebaran(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('𝑺𝒆𝒍𝒂𝒎𝒂𝒕 𝑯𝒂𝒓𝒊 𝑹𝒂𝒚𝒂 𝑰𝒅𝒖𝒍 𝑭𝒊𝒕𝒓𝒊')
    animation_chars = [
        '[Happy Eid Mubarak ](https://telegra.ph/file/f950e09cc4aebcf2abe7f.jpg)',
        '[­🕌](https://telegra.ph/file/506f5aa4870472307f8fd.jpg)',
        '[ㅤ­](https://telegra.ph/file/759966f82f6590a1b8dfa.jpg)',
        '[­ㅤ](https://telegra.ph/file/661ca99916b9cf5a582d6.jpg)',
        '[ㅤ](https://telegra.ph/file/8bec6bbe35d4bd1587569.jpg)',
        '[🕌](https://telegra.ph/file/360ce99e861f8efca1ea3.jpg)',
        '[❣️](https://telegra.ph/file/701503c243265b40e3223.jpg)',
        '[❤️](https://telegra.ph/file/9f0f76eeba3e54298d60a.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@Xa_cmd(pattern="hbd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('𝐻𝑎𝑝𝑝𝑦 𝐵𝑖𝑟𝑡𝒉𝑑𝑎𝑦')
    animation_chars = [
        '[𝐻𝑎𝑝𝑝𝑦 ](https://telegra.ph/file/2fbc53ea22ec4471929fa.jpg)',
        '[­🎉🎉🎉](https://telegra.ph/file/e4e5729634f5c8c0c9e06.jpg)',
        '[𝐵𝑖𝑟𝑡𝒉𝑑𝑎𝑦🎊🎂](https://telegra.ph/file/d60d1697b9ac267371fd6.jpg)',
        '[­𝑇𝑜 𝑌𝑜𝑢🎂](https://telegra.ph/file/0a5d688271f8259b43a9f.jpg)',
        '[𝐻𝑎𝑝𝑝𝑦 𝐵𝑖𝑟𝑡𝒉𝑑𝑎𝑦🎉🎉](https://telegra.ph/file/2fd7cf79f3478ee3c9a27.jpg)',
        '[🎂🎂](https://telegra.ph/file/0f39e15093b70d3502bda.jpg)',
        '[🎁🎈🎈🎉](https://telegra.ph/file/59d6d8e8b1b9d3b112fc3.jpg)',
        '[🎉🎉🎉](https://telegra.ph/file/8021015799addb650f107.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@Xa_cmd(pattern="happyaniv(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('𝐻𝑎𝑝𝑝𝑦 𝐴𝑛𝑖𝑣𝑒𝑟𝑠𝑎𝑟𝑦')
    animation_chars = [
        '[𝐻𝑎𝑝𝑝𝑦 ](https://telegra.ph/file/f0c6b06eb041dddd01119.jpg)',
        '[❤️❤️❤️](https://telegra.ph/file/ebc83df798ba99a94bfc3.jpg)',
        '[𝐴𝑛𝑖𝑣𝑒𝑟𝑠𝑎𝑟𝑦❤️❤️](https://telegra.ph/file/1a302daf9ac95e931b675.jpg)',
        '[­𝑀𝑦 𝑀𝑖𝑛𝑒👩‍❤️‍💋‍👨](https://telegra.ph/file/8a1cba2ab4bbd86609a68.jpg)',
        '[𝐻𝑎𝑝𝑝𝑦 𝐴𝑛𝑖𝑣𝑒𝑟𝑠𝑎𝑟𝑦😻😍💘](https://telegra.ph/file/88a297c386c0c2f999e9c.jpg)',
        '[❤️❤️💘😍](https://telegra.ph/file/f0c6b06eb041dddd01119.jpg)',
        '[💌💌💌❤️](https://telegra.ph/file/59ca0bbaeb740ee58aa72.jpg)',
        '[😍😍😍](https://telegra.ph/file/3cd166b4057b5b60aa71d.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@Xa_cmd(pattern="papku(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('Aku mau ngasih Pap aku buat kamu')
    animation_chars = [
        '[Ini aku](https://telegra.ph/file/091024e9bb4729426cc44.jpg)',
        '[aku ganteng](https://telegra.ph/file/836ec69a83a81b909e106.jpg)',
        '[Ganteng Banget kan 😻](https://telegra.ph/file/597969f9c0783081e523e.jpg)',
        '[­Ganteng intinya👩‍❤️‍💋‍👨](https://telegra.ph/file/32fc29f1689be15e20a7d.jpg)',
        '[Kamu Mau jadi pacarku?😻😍💘](https://telegra.ph/file/0cdcb0452c89a664dcb98.jpg)',
        '[Mau lagi?](https://telegra.ph/file/10140ec996bfed2b41dc1.jpg)',
        '[Nihhh](https://telegra.ph/file/ba17968cd0fa477e96dc3.jpg)',
        '[Terkahir](https://telegra.ph/file/ed6a84a8b1c315183cc35.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)

CMD_HELP.update(
    {
        "ucapan": f"**Plugin : **`ucapan`\
        \n\n    **Perintah :** `{cmd}hbd`\
        \n⌬    **Fungsi : **ucapan selamat ulang tahun.\
        \n\n    **Perintah :** `{cmd}lebaran`\
        \n⌬    **Fungsi : **Ucapan Lebaran.\
        \n\n    **Perintah :** `{cmd}happyaniv`\
        \n⌬    **Fungsi : **Untuk Mengucapkan Happy Aniversary kepasanganmu (Kalo Punya).\
        \n\n    **Perintah :** `{cmd}papku`\
        \n⌬    **Fungsi : **Bonus awoakwoak."
    })
