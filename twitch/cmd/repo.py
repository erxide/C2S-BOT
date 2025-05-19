"""Cmd repo"""
async def repo_cmd(self, ctx):
    """fonction de la cmd repo"""
    await ctx.send(f"Voici le repo du bot : {self.repo_url}")
