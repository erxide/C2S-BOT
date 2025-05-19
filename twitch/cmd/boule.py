"""Cmd boule"""
import random

async def boule_cmd(ctx):
    """fonction de la cmd boule"""
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
