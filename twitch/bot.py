"""Ce script lance le bot twitch C2S"""

import asyncio
import os
import random
import json
from twitchio.ext import commands
from openai import OpenAI
from unidecode import unidecode
from dotenv import load_dotenv

from cmd.c2s import c2s_cmd
from cmd.repo import repo_cmd
from cmd.boule import boule_cmd
from cmd.fesses import fesses_cmd
from cmd.turnOn import turnOn_cmd
from cmd.turnOff import turnOff_cmd
from cmd.gpt import gpt_cmd
from cmd.addPr import addPr_cmd
from cmd.rmPr import rmPr_cmd

load_dotenv()


class C2SBOT(commands.Bot):
    """class du bot twitch"""

    def __init__(self):
        super().__init__(
            token=os.getenv("TWITCH_TOKEN"), prefix="!", initial_channels=["dhalsiiim"]
        )
        self.repo_url = os.getenv("REPO_URL")
        self.turn_off = False
        self.client_openia = OpenAI()
        self.config = self.get_config()

    async def event_ready(self):
        print(f"Connecté au chat Twitch en tant que : {self.nick}")

    def get_config(self):
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)

    async def event_message(self, message):

        if message.echo or message.author.name == "cdeuxs":
            return

        text = unidecode(message.content.lower())

        if self.turn_off and not text.startswith("!turnon"):
            return

        if "quoi" in text.split():
            await message.channel.send(f"@{message.author.name} quoicoubeh")

        if "caca" in text.split():
            await message.channel.send(
                f"@{message.author.name} caca ? comme caca2squidgame mon createur!"
            )

        if len(message.content.split()) >= 30:
            await message.channel.send(
                f"fiouuu y'en a des mots la @{message.author.name}"
            )

        await self.handle_commands(message)

    @commands.command(name="c2s")
    async def c2s_command(self, ctx):
        await c2s_cmd(self, ctx)

    @commands.command(name="repo")
    async def repo_command(self, ctx):
        await repo_cmd(self, ctx)

    @commands.command(name="boule")
    async def boule_de_cristal(self, ctx):
        await boule_cmd(self, ctx)

    @commands.command(name="fesses")
    async def fesses_command(self, ctx):
        await fesses_cmd(self, ctx)

    @commands.command(name="turnOn")
    async def turn_on_command(self, ctx):
        await turnOn_cmd(self, ctx)

    @commands.command(name="turnOff")
    async def turn_off_command(self, ctx):
        await turnOff_cmd(self, ctx)

    @commands.command(name="gpt")
    async def gpt_command(self, ctx):
        await gpt_cmd(self, ctx)

    @commands.command(name="addPr")
    async def add_pr(self, ctx, user: str = None):
        await addPr_cmd(self, ctx, user)

    @commands.command(name="rmPr")
    async def remove_pr(self, ctx, user: str = None):
        await rmPr_cmd(self, ctx, user)


if __name__ == '__main__':
    C2S = C2SBOT()
    C2S.run()
