from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/9b010ead0692e3bc28df6.jpg",
                caption="🦖 **Xa Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @rexaprivateroom ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/tirexgugel"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
