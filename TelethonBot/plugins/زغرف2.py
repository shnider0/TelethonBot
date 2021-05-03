# klanr aloosh To @aaaDa
"""QuotLy: Avaible commands: .zag
"""
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="زغرف"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Subscribe @QADE3im```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Subscribe @QADE3im```")
       return
    chat = "@UJPBOT"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Subscribe @QADE3im```")
       return
    await event.edit("`جار زخرفه النص بحقوق @DEV_F1`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1012712746))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@UJPBOT) u Nigga```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
