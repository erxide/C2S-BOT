import tmi from 'tmi.js';

export const repo_cmd = (BOT:tmi.Client, channel:string, author:string) => {
    console.log(`CMD : ${author} a utilisé la cmd repo`);
    BOT.say(channel, `Voici le repo de C2S : ${process.env.REPO_URL}`);
};