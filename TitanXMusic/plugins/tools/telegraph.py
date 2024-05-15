from telegraph import upload_file
from pyrogram import filters
from TitanXMusic import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "telegraph" , "link"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝐏ʟᴇᴀsᴇ 𝐖ᴀɪᴛ 𝐌ᴀᴋɪɴɢ 𝐀 𝐋ɪɴᴋ 👻")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' 𝐇ᴇʀᴇ 𝐘ᴏᴜʀ 𝐓ᴇʟᴇɢʀᴀᴘʜ 𝐋ɪɴᴋ 😁 {url}')