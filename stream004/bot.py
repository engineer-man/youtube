import asyncio
import websockets
import json

async def message():
	async with websockets.connect('ws://10.0.0.10:3434') as ws:
		while True:
			message = await ws.recv()

			message = json.loads(message)

			if message['message'] == 'hello felix':
				await ws.send(json.dumps({
					'type': 'bot',
					'name': 'felix',
					'message': 'hi friend'
				}))

asyncio.get_event_loop().run_until_complete(message())
