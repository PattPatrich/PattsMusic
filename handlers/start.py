from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2

## ~ Simple Config ~ ##
FRIEND_BOT = "TheNexasMusic_bot"
USER_ACCNAME = "NexaMusicAssistant"



@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

I'm The Nexa Music Bot. Friend of **@{FRIEND_BOT}** 😏️.

I can play Music In Telegram Groups Via Voice Chat! 😌️.

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤨️ How To Use Me 🤨️", url="https://telegra.ph/How-To-Use-Music-Nexa-Bot-03-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

I'm The Nexa Music Bot. Friend of **@{FRIEND_BOT}** 😏️.

I can play Music In Telegram Groups Via Voice Chat! 😌️.

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤨️ How To Use Me 🤨️", url="https://telegra.ph/How-To-Use-Music-Nexa-Bot-03-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command("start@TheNexasMusic_bot") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

I'm The Nexa Music Bot. Friend of **@{FRIEND_BOT}** 😏️.

I can play Music In Telegram Groups Via Voice Chat! 😌️.

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤨️ How To Use Me 🤨️", url="https://telegra.ph/How-To-Use-Music-Nexa-Bot-03-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(command("help") & other_filters2)
async def help(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Bruh! Do you need Help! 🤔️ yea yea I know it! 🙃️

How To Use Me? 🧐️

<b> 1. Add Me and @{USER_ACCNAME} To Your Group!

 2. Give Admin To Me and @{USER_ACCNAME} ! </b>
 
 Enjoy! 😌️

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command("help") & other_filters)
async def help2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Bruh! Do you need Help! 🤔️ yea yea I know it! 🙃️

How To Use Me? 🧐️

<b> 1. Add Me and @{USER_ACCNAME} To Your Group!

 2. Give Admin To Me and @{USER_ACCNAME} ! </b>
 
 Enjoy! 😌️ Also hit /cmdlist to see available commands! 😶️

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )
 

@Client.on_message(command("help@TheNexasMusic_bot") & other_filters)
async def help2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Bruh! Do you need Help! 🤔️ yea yea I know it! 🙃️

How To Use Me? 🧐️

<b> 1. Add Me and @{USER_ACCNAME} To Your Group!

 2. Give Admin To Me and @{USER_ACCNAME} ! </b>
 
 Enjoy! 😌️ Also hit /cmdlist to see available commands! 😶️

Made with ❤️ <b>@NexaBotsUpdates</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command("cmdlist") & other_filters2)
async def cmdlist(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Here is the list of available commands! 😃️

<code>/play</code> - Reply to supported url or "/play supported url"
<code>/skip</code> - Skip currenly playing song!
<code>/pause</code> - Pause currently playing song!
<code>/resume</code> - Resume currently pushed song!
<code>/mute</code> - Mutes Streamer!
<code>/unmute</code> - Unmutes streamer!
<code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
 
 Enjoy! 😌️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👀️ Supported Sites 👀️", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ],
                [
                    InlineKeyboardButton(
                    "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ]
            ]
        )
    )
    
@Client.on_message(command("cmdlist") & other_filters)
async def cmdlist2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Here is the list of available commands! 😃️

<code>/play</code> - Reply to supported url or "/play supported url"
<code>/skip</code> - Skip currenly playing song!
<code>/pause</code> - Pause currently playing song!
<code>/resume</code> - Resume currently pushed song!
<code>/mute</code> - Mutes Streamer!
<code>/unmute</code> - Unmutes streamer!
<code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
 
 Enjoy! 😌️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(command("cmdlist@TheNexasMusic_bot") & other_filters)
async def cmdlist2(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Here is the list of available commands! 😃️

<code>/play</code> - Reply to supported url or "/play supported url"
<code>/skip</code> - Skip currenly playing song!
<code>/pause</code> - Pause currently playing song!
<code>/resume</code> - Resume currently pushed song!
<code>/mute</code> - Mutes Streamer!
<code>/unmute</code> - Unmutes streamer!
<code>/vc</code> - Give voice chat link of your group! (Only For Public Groups)
 
 Enjoy! 😌️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
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

<b><a href="https://github.com/CallsMusic">CallsMusic</a></b> - For Callsmusic (Main Code ❤️) !
<b><a href="https://github.com/nikhileashy">N A C</a></b> - For <code>/vc</code> Command

Made with ❤️ by **@NexaBotsUpdates**

Respect To Code Owners! Not To Me!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )   



@Client.on_message(command("vc") & other_filters)
async def vc(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>


             😌️  **Voice Chat Link** 😌️
____________________------------______________________

👉️ https://t.me/{message.chat.username}?voicechat   👈️
____________________------------______________________

Enjoy!😌️❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(command("vc@TheNexasMusic_bot") & other_filters)
async def vc(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>


             😌️  **Voice Chat Link** 😌️
____________________------------______________________

👉️ https://t.me/{message.chat.username}?voicechat   👈️
____________________------------______________________

Enjoy!😌️❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Update Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )
    

@Client.on_message(command("search") & other_filters2)
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
    
 
@Client.on_message(command("search@TheNexasMusic_bot") & other_filters)
async def search2(_, message: Message):
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


@Client.on_message(command("search") & other_filters)
async def search2(_, message: Message):
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


    
