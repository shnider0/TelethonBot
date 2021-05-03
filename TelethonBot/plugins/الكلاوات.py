"""Emoji

Available Commands:

.br

if u edit it then u r gay"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.7

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "kla":

        await event.edit(input_str)

        animation_chars = [
        
            "انته", 
            "انته وين", 
            "انته وين لكيت", 
            "انته وين لكيت هاي", 
            "انته وين لكيت هاي الكلاوات ", 
            "انته وين لكيت هاي الكلاوات بعد قلبي"
 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
