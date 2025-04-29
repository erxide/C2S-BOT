"""Ce script lance le bot twitch C2S"""

import os
import random
from twitchio.ext import commands
from openai import OpenAI
from unidecode import unidecode
from dotenv import load_dotenv

load_dotenv()

ADMIN = ["caca2squidgame", "dhalsiiim"]


class Bot(commands.Bot):
    """class du bot twitch"""

    def __init__(self):
        super().__init__(
            token=os.getenv("TWITCH_TOKEN"), prefix="!", initial_channels=["dhalsiiim"]
        )
        self.repo_url = os.getenv("REPO_URL")
        self.turn_off = False
        self.client_openia = OpenAI()

    async def event_ready(self):
        print(f"Connecté au chat Twitch en tant que : {self.nick}")

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
        """commande c2s"""
        await ctx.send("C2S powered 😎")

    @commands.command(name="repo")
    async def repo_command(self, ctx):
        """commande repo"""
        await ctx.send(f"Voici le repo du bot : {self.repo_url}")

    @commands.command(name="boule")
    async def boule_de_cristal(self, ctx):
        """commande boule"""
        reponses = [
            "Oui, clairement ! 🔮",
            "Non, sûrement pas. ❌",
            "Les astres sont confus... 🤔",
            "Probablement oui ! 🌟",
            "Hmm... c'est un grand OUI du destin. ✅",
            "Pas pour l’instant, mais persévère ! 💪",
            "C’est écrit dans les étoiles... peut-être 🌠",
        ]

        await ctx.send(f"@{ctx.author.name} {random.choice(reponses)}")

    @commands.command(name="fesses")
    async def fesses_command(self, ctx):
        """commande fesses"""
        if ctx.author.name in ADMIN:
            await ctx.send(
                "SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss " 
                "SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss " 
                "SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss " 
                "SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss "
                "SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss "
                "SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss SSSsss "
                "SSSsss SSSsss SSSsss SSSsss SSSsss"
            )
        else:
            await ctx.send("fesses")

    @commands.command(name="turnOn")
    async def turn_on_command(self, ctx):
        """commande turn on"""
        if ctx.author.name in ADMIN:
            self.turn_off = False
            await ctx.send("Je suis de retour ^^")

    @commands.command(name="turnOff")
    async def turn_off_command(self, ctx):
        """commande turn off"""
        if ctx.author.name in ADMIN:
            self.turn_off = True
            await ctx.send("Salut a la prochaine")

    @commands.command(name="gpt")
    async def gpt_command(self, ctx):
        """commande gpt"""
        if ctx.author.name in ADMIN:
            user_input = (
                "donne une réponse courte : "
                + ctx.message.content[len(ctx.prefix) + len(ctx.command.name) + 1 :]
            )

            response = self.client_openia.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=100,
            )

            gpt_text = response.choices[0].message.content.strip()

            await ctx.send(f"@{ctx.author.name} {gpt_text[:480]}")


bot = Bot()
bot.run()
