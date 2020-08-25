from time import sleep
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Biasakanlah Mengucapkan Salam")
    sleep(1)
    await typew.edit("Assalamualaikum")

CMD_HELP.update({
    "p": ".P\
    \nUsage: Type .P untuk type Salam. "
})



