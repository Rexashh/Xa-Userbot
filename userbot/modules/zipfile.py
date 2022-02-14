import asyncio
import zipfile
from datetime import date
import time
import os
from userbot import TEMP_DOWNLOAD_DIRECTORY, ZIP_DOWNLOAD_DIRECTORY, bot, CMD_HELP
from userbot.utils import progress
from userbot.events import rose_cmd
from userbot import CMD_HANDLER as cmd
# ====================
today = date.today()
# ====================


@bot.on(rose_cmd(outgoing=True, pattern=r"compress(?: |$)(.*)"))
async def _(event):
    # Prevent Channel Bug to use update
    if event.is_channel and not event.is_group:
        await event.edit("️✖️ `Perintah Kompres tidak diizinkan di saluran...`")
        return
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("📂 `Balas ke file untuk mengompresnya...`")
        return
    mone = await event.edit("`Pengolahan...`")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[DOWNLOADING]")
                ),
            )
            directory_name = downloaded_file_name
            await event.edit(
                f"📂 Diunduh ke `{directory_name}`" "`\n`mengompresi file...`"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
    zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
        directory_name
    )
    c_time = time.time()
    await bot.send_file(
        event.chat_id,
        directory_name + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[UPLOADING]")
        ),
    )
    await event.edit("✔️`Selesai!!`")
    await asyncio.sleep(7)
    await event.delete()


@bot.on(rose_cmd(outgoing=True, pattern=r"addzip(?: |$)(.*)"))
async def addzip(add):
    """ Copyright (c) 2020 azrim @github"""
    # Prevent Channel Bug to use update
    if add.is_channel and not add.is_group:
        await add.edit("✖️ `Perintah tidak diizinkan di saluran...`")
        return
    if add.fwd_from:
        return
    if not add.is_reply:
        await add.edit("📂 `Balas ke file untuk mengompresnya...`")
        return
    mone = await add.edit("`Pengolahan...`")
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        os.makedirs(ZIP_DOWNLOAD_DIRECTORY)
    if add.reply_to_msg_id:
        reply_message = await add.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                ZIP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[DOWNLOADING]")
                ),
            )
            success = str(downloaded_file_name).replace("./zips/", "")
            await add.edit(f"✔️ `{success} Berhasil ditambahkan ke daftar!`")
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return


@bot.on(rose_cmd(outgoing=True, pattern=r"upzip(?: |$)(.*)"))
async def upload_zip(up):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await up.edit("✖️`File tidak ditemukan!`")
        return
    mone = await up.edit("📂`File zip...`")
    input_str = up.pattern_match.group(1)
    curdate = today.strftime("%m%d%y")
    title = str(input_str) if input_str else "zipfile" + f"{curdate}"
    zipf = zipfile.ZipFile(title + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(ZIP_DOWNLOAD_DIRECTORY, zipf)
    zipf.close()
    c_time = time.time()
    await bot.send_file(
        up.chat_id,
        title + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=up.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[UPLOADING]", input_str)
        ),
    )
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await up.delete()


@bot.on(rose_cmd(outgoing=True, pattern=r"rmzip(?: |$)(.*)"))
async def remove_dir(rm):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await rm.edit("😔`Direktori tidak ditemukan!`")
        return
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await rm.edit("💣`Daftar pos dihapus!`")


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))


CMD_HELP.update({
    "zipfile":
    f"**✘ Plugin** `zipfile` :\
\n\n  •  **Perintah :** `{cmd}compress` [**Membalas File**]\
  \n  •  **Fungsi : **Buat File Menjadi Zip.\
\n\n  •  **Perintah :** `{cmd}addzip` [**Membalas File**]\
  \n  •  **Fungsi : **Tambahkan File ke Daftar Zip.\
\n\n  •  **Perintah :** `{cmd}upzip` [**Judul zip**]\
  \n  •  **Fungsi : **Unggah Daftar zip.\
\n\n  •  **Perintah :** `{cmd}rmzip` [**Judul zip**]\
  \n  •  **Fungsi : **Hapus Daftar zip."})
