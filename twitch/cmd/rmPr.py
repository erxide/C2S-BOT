import json

async def rmPr_cmd(self, ctx, user: str = None):
    if ctx.author.name in self.config['ADMIN']:
        if user is None:
            await ctx.send("Veuillez spécifier un utilisateur. Exemple : !rmPr @misty_toonz")
            return

        username = user.lstrip("@")

        if username not in self.config['PRENIUM']:
            await ctx.send(f"{username} n'est pas dans le groupe PRENIUM.")
            return

        self.config['PRENIUM'].remove(username)

        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

        self.config = self.get_config()

        await ctx.send(f"@{ctx.author.name} @{username} a été retiré du groupe PRENIUM.")