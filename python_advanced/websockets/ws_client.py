#!/usr/bin/env python3
"""Simple websocket client."""
import os
import asyncio
import websockets


async def connect_and_send(uri, text):
    async with websockets.connect(uri) as socket:
        await socket.send(text)
        return await socket.recv()


async def main():
    response = await connect_and_send(
            "ws://localhost:8765",
            "Hello WebSocket"
    )
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
