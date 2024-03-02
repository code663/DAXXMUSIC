import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import RPCError
from typing import Union, Optional
from pyrogram import filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app  

photo = [
    "https://telegra.ph/file/466152f38c4fa1d30a8ce.jpg",
    "https://telegra.ph/file/72369c352587c54e5aaff.jpg",
    "https://telegra.ph/file/057827d334a75103016b2.jpg",
    "https://telegra.ph/file/8d4df841cc3db656dc5d6.jpg",
    "https://telegra.ph/file/22cbc045071a2b046a848.jpg",
    "https://telegra.ph/file/de0422c51cdef3fd8a508.jpg",
    "https://telegra.ph/file/d5a8b909b9cb7d3bdb6d8.jpg",
    "https://telegra.ph/file/7d6dcf74e4fa529b311af.jpg",
    "https://telegra.ph/file/21c69049c4855ac0a035b.jpg",
    "https://telegra.ph/file/35cafae38a333d70a7a30.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❀\n\n"
               
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {message.chat.id}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠[ʙᴀʙʏ ᴛᴏᴜᴄʜ]({link})\n"
                f"๏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠ {count}\n"
                f"๏ ᴀᴅᴅᴇᴅ ʙʏ ➠ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"↻ sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ ↻", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❀ <b><u>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</u></b> ❀\n\n๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n\n๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n\n๏ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n\n๏ ʙᴏᴛ ɴᴀᴍᴇ ➠ @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❀ ʜᴇʏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ❀\n\n"
                
                f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"๏ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"๏ ʏᴏᴜʀ ɪᴅ ➠ {member.id}\n"
                f"๏ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ ➠ @{member.username}\n"
                f"๏ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛᴏᴛᴇʟ {count} ᴍᴇᴍʙᴇʀs ๏"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"↻ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ↻", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):

    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {
            "banned", "left", "restricted"
        }
        and member.old_chat_member
    ):
        pass
    else:
        return

    user = (
        member.old_chat_member.user
        if member.old_chat_member
        else member.from_user
    )


            caption = f"**ᴀ ᴍᴇᴍʙᴇʀ ʟᴇғᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🥹\n\n✧══════•❁❀❁•══════✧\n╠╼➪ ✨ 𝐍𝐀𝐌𝐄 = {user.mention}\n╠╼➪ 💫 𝐔𝐒𝐄𝐑 𝐈𝐃 = {user.id}\n╠╼➪  🎁 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 = @{user.username}\n✧══════•❁❀❁•══════✧\n\n๏sᴇᴇ ʏᴏᴜ sᴏᴏɴ ᴀɢᴀɪɴ..!**"
            button_text = " Kɪᴅɴᴀᴘ ᴍᴇ 🥹 "

            
            deep_link = f"https://t.me/{app.username}?startgroup=true"

            
            await client.send_photo(
                chat_id=member.chat.id,
                photo=random.choice(photo),
                caption=caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)]
                ])
)

        except RPCError as e:
            print(e)
            return
    

