import asyncio
from utils.split_by_words import split_by_words

async def gpt_cmd(self, ctx):
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

        chunks = split_by_words(gpt_text)

        for chunk in chunks:
            await ctx.send(f"@{ctx.author.name} {chunk}")
            await asyncio.sleep(1) 