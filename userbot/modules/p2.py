from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Nah Gitu ")
    sleep(1)
    await typew.edit(Waalaikumsalam")
