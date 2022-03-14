import asyncio
import websockets
import json

async def make_request():
    async with websockets.connect("ws://localhost:4444") as websocket:
        await websocket.send(json.dumps({"request-type":"SetCurrentScene","scene-name":"Scene 2","message-id":"1"}))
        print(await websocket.recv())
        

asyncio.run(make_request())
