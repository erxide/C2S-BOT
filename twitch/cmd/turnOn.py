async def turnOn_cmd(self, ctx):
    if ctx.author.name in self.config['ADMIN']:
        self.turn_off = False
        await ctx.send("Je suis de retour ^^")