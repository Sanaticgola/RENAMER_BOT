from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	 HEY DUDE 🤘{message.from_user.first_name }
	__I am fast file renamer bot, Please send any telegram 
	**Document Or Video** and enter new filename__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("SUPPORT US" ,url="https://t.me/Sanaticsmovies"), 
	  InlineKeyboardButton("CHANNEL", url="https://t.me/Sanaticsmovies")
         ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("✏ RENAME ✏",callback_data = "rename")
       ,InlineKeyboardButton("❌ CANCEL ❌",callback_data = "cancel")  ]]))
