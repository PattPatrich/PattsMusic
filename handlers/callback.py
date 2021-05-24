from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from handlers.start import FRIEND_BOT

# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


# Start callback 

@Client.on_callback_query(filters.regex("startcb"))
async def startcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hey 😉️!</b>
I'm Patt's Music Bot. Friend of **@{FRIEND_BOT}** 😏️.
I can play Music In Telegram Groups Via Voice Chat! 😌️.
Made with ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤨️ How To Use Me 🤨️", url="https://telegra.ph/How-To-Use-Patts-Music-Bot-05-23"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ Join IsItIsAsItIs 🔰️", url="https://t.me/IsItIsAsItIs"
                    )
            ]
        )
    )
    

# Command list callback

@Client.on_callback_query(filters.regex("cmdlistcb"))
async def cmdlistcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hey 😉️!</b>

Here is the list of available commands! 😃️

• **Group Admin Only Commands 👮 ✓,**

 ➲ <code>/play</code> - Reply to supported url or "/play supported url"
 ➲ <code>/skip</code> - Skip currenly playing song!
 ➲ <code>/pause</code> - Pause currently playing song!
 ➲ <code>/resume</code> - Resume currently pushed song!
 ➲ <code>/mute</code> - Mutes Streamer!
 ➲ <code>/unmute</code> - Unmutes streamer!
 ➲ <code>/joingrp</code> - To Add Streamer Account To Your Group!
 ➲ <code>/leavegrp</code> - To Remove Streamer Account From Your Group!


• **Group Members Commands 👮 ✓,**

 ➲ <code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
 ➲ <code>/yts (song name)</code> - Download song by it's name!
 ➲ <code>/ytvid (song name)</code> - Download Videos From YouTube!
 ➲ <code>/saavn (song name)</code> - Download Songs From Saavn!
 ➲ <code>/deezer (song namme)</code> - Download Songs From Deezer!

**❌ Don't End Voice Chat While Bot Playing A Song ❌**

Made with ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👀️ Supported Sites 👀️", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⟲ Go Back ⟲", callback_data="startcb"
                    )
                ]
            ]
        )
    )
