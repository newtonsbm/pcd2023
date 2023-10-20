import asyncio
import json
from datetime import datetime
from websockets.server import serve
from rich import print

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8765

USERS = []
html_tmpl = "<div id='chat' hx-swap-oob='beforeend'>{message}<br></div>"

async def broadcast(message):
    for user in USERS:
        await user.send(message)


async def process_message(json_message):
    """process htmx json websocket message"""
    message_obj = json.loads(json_message)
    message = message_obj['message']
    return message


async def chat(websocket, path):
    # get first message from client
    first_message = True
    name = "Anonimo"
    USERS.append(websocket)
    async for message_json in websocket:
        message = await process_message(message_json)
        if first_message:
            name = message
            new_msg = f"{name} entrou na sala!"
            first_message = False
        else:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            new_msg = f"{now} - {name} disse: {message}"
        print(new_msg)
        html_message = html_tmpl.format(message=new_msg)
        await broadcast(html_message)
    USERS.remove(websocket)
    bye_message = f"{name} saiu da sala!"
    print(bye_message)
    html_bye_message = html_tmpl.format(message=bye_message)
    await broadcast(html_bye_message)

async def main():
    print("Iniciando servidor...")
    print(f"Servidor rodando em [bold magenta]ws://{SERVER_HOST}:{SERVER_PORT}[/bold magenta]")
    async with serve(chat, SERVER_HOST, SERVER_PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())