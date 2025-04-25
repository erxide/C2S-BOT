"""Ce script lance le bot Discord C2S"""

import os
import sys
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN_BOT = os.getenv("TOKEN_DISCORD")
REPO_URL = os.getenv("REPO_URL")

if TOKEN_BOT is None or REPO_URL is None:
    print("Probleme d'importation .env")
    sys.exit(1)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=None, intents=intents)


@bot.event
async def on_ready():
    """Déclenché lorsque le bot est connecté et prêt."""
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées ({len(synced)} commandes).")
    except discord.HTTPException as e:
        print(f"Erreur de sync ({type(e).__name__}): {e}")


@bot.event
async def on_message(message):
    """Repond quoicoubeh lorsqu'un user dit quoi"""
    if message.author == bot.user:
        return

    contenu = message.content.lower()

    if "quoi" in contenu.split():
        await message.reply("quoicoubeh")


@bot.tree.command(name="repo", description="Affiche l'URL du dépôt GitHub du bot.")
async def repo_command(interaction: discord.Interaction):
    """Command pour afficher le lien du repo du projet"""
    await interaction.response.send_message(
        f"Voici le repo du bot : {REPO_URL}", ephemeral=False
    )


if __name__ == "__main__":
    bot.run(TOKEN_BOT)
