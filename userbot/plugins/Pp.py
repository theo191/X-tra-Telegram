# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.pp", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("PayPal.me/endshop"))
	
    
