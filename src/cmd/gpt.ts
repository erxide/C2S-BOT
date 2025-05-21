import tmi from 'tmi.js';
import type { Config } from '../types';
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

export const gpt_cmd = async (BOT:tmi.Client, channel:string, author:string, config:Config, message:string) => {
    console.log(`CMD : ${author} a utilisé la cmd gpt`);
    if (config.ADMIN.includes(author) || config.PRENIUM.includes(author)) {
        const userInput = message.slice('!gpt'.length).trim();
        const prompt = 'donne une réponse courte : ' + userInput;

        const reponse = await openai.chat.completions.create({
            model: 'gpt-4-1106-preview',
            messages: [{role: 'user', content: prompt}],
            max_tokens: 200
        });

        const gptText = reponse.choices[0]?.message?.content?.trim();
        if (!gptText) return;

        BOT.say(channel, `@${author} ${gptText}`);
    }
};