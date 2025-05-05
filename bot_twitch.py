"""Ce script lance le bot twitch C2S"""

import asyncio
import os
import random
import json
from twitchio.ext import commands
from openai import OpenAI
from unidecode import unidecode
from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):
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
        with open("config-twitch.json", "r", encoding="utf-8") as f:
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

    def split_by_words(self, text, max_length=480):
        words = text.split()
        chunks = []
        current = ""

        for word in words:
            if len(current) + len(word) + 1 <= max_length:
                current += (" " if current else "") + word
            else:
                chunks.append(current)
                current = word

        if current:
            chunks.append(current)

        return chunks

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
        if ctx.author.name in self.config['ADMIN'] or ctx.author.name in self.config['PRENIUM']:
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
        if ctx.author.name in self.config['ADMIN']:
            self.turn_off = False
            await ctx.send("Je suis de retour ^^")

    @commands.command(name="turnOff")
    async def turn_off_command(self, ctx):
        """commande turn off"""
        if ctx.author.name in self.config['ADMIN']:
            self.turn_off = True
            await ctx.send("Salut a la prochaine")

    @commands.command(name="gpt")
    async def gpt_command(self, ctx):
        """commande gpt"""
        if ctx.author.name in self.config['ADMIN'] or ctx.author.name in self.config['PRENIUM']:
            user_input = (
                "donne une réponse courte : "
                + ctx.message.content[len(ctx.prefix) + len(ctx.command.name) + 1 :]
            )

            response = self.client_openia.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=500,
            )

            gpt_text = response.choices[0].message.content.strip()

            chunks = self.split_by_words(gpt_text)

            for chunk in chunks:
                await ctx.send(f"@{ctx.author.name} {chunk}")
                await asyncio.sleep(1) 

    @commands.command(name="addPr")
    async def add_pr(self, ctx, user: str = None):
        if ctx.author.name in self.config['ADMIN']:
            if user is None :
                await ctx.send("Veuillez spécifier un utilisateur. Exemple : !addPr @misty_toonz")
                return
            
            username = user.lstrip("@")

            if username in self.config['PRENIUM']:
                await ctx.send(f"{username} est déjà dans le groupe PRENIUM.")
                return

            self.config['PRENIUM'].append(username)

            with open("config-twitch.json", "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)

            self.config = self.get_config()

            await ctx.send(f"@{ctx.author.name} @{username} a été ajouté au groupe PRENIUM.")

    @commands.command(name="rmPr")
    async def remove_pr(self, ctx, user: str = None):
        if ctx.author.name in self.config['ADMIN']:
            if user is None:
                await ctx.send("Veuillez spécifier un utilisateur. Exemple : !rmPr @misty_toonz")
                return

            username = user.lstrip("@")

            if username not in self.config['PRENIUM']:
                await ctx.send(f"{username} n'est pas dans le groupe PRENIUM.")
                return

            self.config['PRENIUM'].remove(username)

            with open("config-twitch.json", "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)

            self.config = self.get_config()

            await ctx.send(f"@{ctx.author.name} @{username} a été retiré du groupe PRENIUM.")

bot = Bot()
bot.run()
