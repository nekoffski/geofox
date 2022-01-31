import typing
import asyncio
import random
import os

import discord
import youtube_dl as yt
from discord.ext import commands


token = os.getenv("geofox-token")


class MusicPlayer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue: typing.List[str] = []

    @commands.command()
    async def join(self, ctx: commands.Context):
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
            return

        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await ctx.send("Joining to channel")
            await channel.connect()
        else:
            await ctx.send("Switching to channel")
            await ctx.voice_client.move_to(channel)

    @commands.command()
    async def disconnect(self, ctx: commands.Context):
        await ctx.send("Disconnecting")
        await ctx.voice_client.disconnect()

    @commands.command()
    async def shuffle(self, ctx: commands.Context):
        await ctx.send(f"Shuffling songs queue, songs in queue: {len(self.queue)}")
        random.shuffle(self.queue)

    @commands.command()
    async def add(self, ctx: commands.Context, url: str):
        ydl_options = {
            'format': 'bestaudio'
        }

        async def load_audio(info):
            url = info['formats'][0]['url']

            ffmpeg_options = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'
            }

            await ctx.send(f"Song {info['title']} added to the playing queue")

            source = await discord.FFmpegOpusAudio.from_probe(url, **ffmpeg_options)
            self.queue.append(source)

        async def load_playlist(infos):
            print("Loading playlist")

            tasks = [load_audio(info) for info in infos]
            await asyncio.gather(*tasks)

        with yt.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                await load_playlist(info['entries'])
            else:
                await load_audio(info)

    @commands.command()
    async def play(self, ctx: commands.Context):
        voice_client: discord.VoiceChannel = ctx.voice_client
        voice_client.stop()

        # if voice_client.is_playing:
        # await ctx.send("Already playing")
        # return

        def play_audio(ctx: commands.Context):
            if len(self.queue) == 0:
                asyncio.run_coroutine_threadsafe(
                    ctx.send("There is nothing to play, queue is empty"), asyncio.get_event_loop())
                return

            source = self.queue.pop(0)
            voice_client.play(source, after=lambda _: play_audio(ctx))

        play_audio(ctx)

    @commands.command()
    async def pause(self, ctx: commands.Context):
        await ctx.send("Pausing")
        ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx: commands.Context):
        await ctx.send("Resuming")
        ctx.voice_client.resume()


def main():
    client = commands.Bot(command_prefix="*")
    client.remove_command("help")

    cogs = [
        MusicPlayer(client)
    ]

    for cog in cogs:
        client.add_cog(cog)

    @client.command()
    async def help(ctx: commands.Context):
        await ctx.channel.send("TODO")

    @client.command()
    async def me(ctx: commands.Context):
        me_msg = "Foxes & Geologists discord bot, implemented in python3.9 & discord.py with <3 by nyeko and spułka"
        await ctx.channel.send(me_msg)

    client.run(token)


if __name__ == '__main__':
    main()
