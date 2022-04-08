

from userbot.utils import Xa_cmd
import asyncio
# BY Sh1vam Dont try to kang
# Ported by @JustRex


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
