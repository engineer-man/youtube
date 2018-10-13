import asyncio
import websockets

clients = []

async def new_conn(ws, path):
	clients.append(ws)
	while True:
		try:
			message = await ws.recv()
		except:
			return
		for client in clients:
			try:
				await client.send(message)
			except:
				continue

server = websockets.serve(new_conn, '0.0.0.0', 3434)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
