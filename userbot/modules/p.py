from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Biasakanlah Mengucapkan Salam")
    sleep(1)
    await typew.edit("Assalamualaikum")
# Create by myself @AkameNFS
