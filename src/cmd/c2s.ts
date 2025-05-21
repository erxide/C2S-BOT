import tmi from 'tmi.js';

export const c2s_cmd = (BOT:tmi.Client, channel:string, author:string) => {
    console.log(`CMD : ${author} a utilisé la cmd c2s`);
    BOT.say(channel, 'C2S powered 😎');
};