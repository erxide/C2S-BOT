async def turnOff_cmd(self, ctx):
    if ctx.author.name in self.config['ADMIN']:
        self.turn_off = True
        await ctx.send("Salut a la prochaine")