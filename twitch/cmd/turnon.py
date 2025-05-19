"""Cmd turnOn"""
async def turnon_cmd(self, ctx):
    """fonction de la cmd turnOn"""
    if ctx.author.name in self.config['ADMIN']:
        self.turn_off = False
        await ctx.send("Je suis de retour ^^")
