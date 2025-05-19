"""Cmd fesses"""
async def fesses_cmd(self, ctx):
    """fonction de la cmd fesses"""
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
