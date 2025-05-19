"""Cmd turnOff"""
async def turnoff_cmd(self, ctx):
    """fonction de la cmd turnOff"""
    if ctx.author.name in self.config['ADMIN']:
        self.turn_off = True
        await ctx.send("Salut a la prochaine")
