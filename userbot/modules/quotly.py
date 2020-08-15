# port to userbot by @MoveAngel

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.q(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Balas Ke Pesan Siapapun.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("Balas Ke Teks")
        return
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Balas Ke Pesan Pengguna.")
        return
    await event.edit("Membuat Text Menjadi Stiker\n**NFS乛Rizky戈手**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1031952739))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Tolong Unblock @QuotLyBot Dan Coba Lagi")
            return
        if response.text.startswith("Hi!"):
            await event.edit("Bisakah Kamu Meminta Kepada Admin Untuk Mengizinkan Foward?")
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)

CMD_HELP.update({
    "quotly":
        ".q \
          \nUsage: Enhance ur text to sticker.\n"
})
