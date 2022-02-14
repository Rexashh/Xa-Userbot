# Port By @VckyouuBitch From Geez-Project
# Credits © Geez - projects

import os
import urllib

from telethon.tl import functions
from userbot.events import rose_cmd
from userbot import (
    CMD_HELP,
    bot,
    ALIVE_NAME,
)
from userbot import CMD_HANDLER as cmd
from userbot import TEMP_DOWNLOAD_DIRECTORY


OFFLINE_TAG = f"{ALIVE_NAME} #OFFLINE"
ONLINE_TAG = f"{ALIVE_NAME} #ONLINE"
PROFILE_IMAGE = os.environ.get(
    "PROFILE_IMAGE", "https://telegra.ph/file/3151c4958f5c1be363faf.jpg"
)


@bot.on(rose_cmd(outgoing=True, pattern=r"offline(?: |$)(.*)"))
# pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Sudah dalam Mode Offline.**")
        return
    await event.edit("**Mengubah Profil menjadi Offline...**")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(
        "https://https://telegra.ph/file/3151c4958f5c1be363faf.jpg", "donottouch.jpg"
    )
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit("**Changed profile to OffLine.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    last_name = ""
    first_name = OFFLINE_TAG
    try:
        await bot(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Offline now.**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@bot.on(rose_cmd(outgoing=True, pattern=r"unoff(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Changing Profile to Online...**")
    else:
        await event.edit("**Sudah Online.**")
        return
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(PROFILE_IMAGE, "donottouch.jpg")
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit("**Mengubah profil menjadi Online.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    first_name = ONLINE_TAG
    last_name = ""
    try:
        await bot(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Online !**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


CMD_HELP.update({
    "mystatus":
    f"✘ **Plugin mystatus** :\
\n\n  •  **Perintah** : `{cmd}offline` \
  \n  •  **Fungsi** : Tambahkan tag offline di nama Anda dan ubah foto profil menjadi hitam.\
\n\n  •  **Perintah** : `{cmd}unoff` \
  \n  •  **Fungsi** : Hapus Tag Offline dari nama Anda dan ubah foto profil menjadi `{cmd}set var PROFILE_IMAGE` [link]."})
