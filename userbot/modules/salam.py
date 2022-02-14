from platform import uname
from userbot import ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇....SAYANG!!!!")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......")


@register(outgoing=True, pattern='^K(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI PERKENALKAN NAMA SAYA GAK TAU LUPA!!**")


@register(outgoing=True, pattern='^ps(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GIMANA KABAR KAMU SAYANG??APAKAH BAIK?**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ELEEEHHHH SOK BANGET KEPINTERAN KAMU!!**")


@register(outgoing=True, pattern='^ds(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NGOPI BOS NGOPI JANGAN DIAM DIAM BAE!!**")


@register(outgoing=True, pattern='^gc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**INI GRUB APA KUBURAN SEPI BANGET ASTAGFIRULLAH!!**")


@register(outgoing=True, pattern='^yu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAN UDAH GUA BILANG??MAKANYA JANGAN NGEYEL!!**")


@register(outgoing=True, pattern='^kr(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH KAMU!!**")


@register(outgoing=True, pattern='^kj(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MACAM BAGUS AE LU BEGITU HMM!!**")


@register(outgoing=True, pattern='^hh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAAF BUKAN JAGOAN HAHAHAHA!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BISMILLAH SLEEP CALL!!😁**")


@register(outgoing=True, pattern='^gb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GANTENG LU BEGITU???**")


@register(outgoing=True, pattern='^war(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**War War Tai anjing, Ketrigger minta sharelok, Udah di sharelok Ga nyamperin,Keras di sosmed Bhakss...**")


@register(outgoing=True, pattern='^ch(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CANTIK LU BEGITU???**")


@register(outgoing=True, pattern='^mb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MENTANG MENTANG PUNYA BOT MAINNYA BOT!!PANTES MUKANYA KAYA BOT😁**")


@register(outgoing=True, pattern='^gs(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EMANG HARUS GITU BGT YA?!!SERIUS HARUS GITU? AWOAKWOAK**")
