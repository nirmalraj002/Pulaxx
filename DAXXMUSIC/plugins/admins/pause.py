from pyrogram import filters
from pyrogram.types import Message

from DAXXMUSIC import app
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.utils.database import is_music_playing, music_off
from DAXXMUSIC.utils.decorators import AdminRightsCheck
from DAXXMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await DAXX.pause_stream(chat_id)
    photo_url = "https://te.legra.ph/file/10428b65648494b3c6ede.jpg"  # Replace with the URL of the photo you want to send
    caption = _["admin_2"].format(message.from_user.mention)
    await message.reply_photo(
        photo=photo_url,                
    )
    await message.reply_text(text=caption)
