from BanAllBot import app,BOT_ID,SUDO
from pyrogram import filters,enums


@app.on_message(filters.command("tagall") & filters.user(SUDO))
async def ban_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.ban_chat_member(chat_id, member.user.id)
                    await msg.reply_text(f"Hallo Gaes.. izin tagall 😘❤️ {member.user.mention}")                    
            except Exception:
                pass
    else:
        await msg.reply_text("𝐀ʙᴇ 𝐋ᴏᴠᴅᴇ 𝐌ᴀᴛʜᴇʀᴄʜᴏᴅ 𝐁ʜᴀᴋ ")  
                                         
    
            
