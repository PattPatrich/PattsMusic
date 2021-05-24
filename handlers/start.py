import os

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2


## ~ Simple Config ~ ##
FRIEND_BOT = "IsItIsAsItIsMusicBot"
USER_ACCNAME = os.getenv("USER_ACCNAME", "PattsMusicAssistant")


@Client.on_message(command(["start", "start@PattsMusicBot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

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
                        "🔰️ Join IsItAsItIs 🔰️", url="https://t.me/IsItIsAsItIs"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(command(["help", "help@PattsMusicBot"]))
async def help(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Bruh! Do you need Help! 🤔️ yea yea I know it! 🙃️

How To Use Me? 🧐️

<b> 1. Add Me and @{USER_ACCNAME} To Your Group! (Send `/joingrp` to your group! Streamer Will Automatically join)

 2. Give Admin To Me and @{USER_ACCNAME} ! </b>

 
**For More Info or Know about My Commands Just Click On "♻️ Additional Help ♻️" Button!**

Made with ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♻️ Additional Help ♻️", callback_data="cmdlistcb"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Join IsItIsAsItIs ⚜️", url="https://t.me/IsItIsAsItIs"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["cmdlist", "cmdlist@PattsMusicBot"]))
async def cmdlist(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

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
                        "⚜️ Join IsItIsAsItIs ⚜️", url="https://t.me/IsItIsAsItIs"
                    )
                ]
            ]
        )
    )
   
    
@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

__Note!__ ⚠️: This Project Is <b>Not Fully Owned By Me</b> !

Credits To,

<b><a href="https://github.com/Itz-fork/">CallsMusic</a></b> - For Editted code
<b><a href="https://github.com/CallsMusic">CallsMusic</a></b> - For Callsmusic (Main Code ❤️) !
<b>Mr Dark Prince</b> - For Yt Download!
<b>TheHamkercat</b> - For Deezer and Saavn Download!
<b>TeamDaisyX</b>
<b>N A C</b> - For <code>/vc</code> Command

Made with ❤️

Respect To Code Owners! Not To Me!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜️ Join IsItIsAsIs ⚜️", url="https://t.me/IsItIsAsItIs"
                    )
                ]
            ]
        )
    )   


@Client.on_message(command(["vc", "vc@PattsMusicBot"]) & other_filters)
async def vc(_, message: Message):
    VC_LINK = f"https://t.me/{message.chat.username}?voicechat"
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>


             😌️  **Voice Chat Link** 😌️
____________________------------______________________

👉️ [Here Is Your Voice Chat Link](https://t.me/{message.chat.username}?voicechat) 👈️
____________________------------______________________

Enjoy!😌️❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "↗️ Share Voice Chat Invitation ↗️", url=f"https://t.me/share/url?url=**Join%20Our%20Group%20Voice%20Chat%20😉%20%20{VC_LINK}%20❤️**"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ Join IsItIsAsItIs 🔰️", url="https://t.me/IsItIsAsItIs"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command(["search", "search@PattsMusicBot"]))
async def search(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yeah", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Nope ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
