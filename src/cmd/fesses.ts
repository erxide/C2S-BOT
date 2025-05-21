import tmi from 'tmi.js';
import type { Config } from '../types';

export const fesses_cmd = (BOT:tmi.Client, channel:string, author:string, config:Config) => {
    console.log(`CMD : ${author} a utilisé la cmd fesses`);
    if (config.ADMIN.includes(author) || config.PRENIUM.includes(author)) {
        BOT.say(channel, 'SSSsss '.repeat(71).trim());
    } else {
        BOT.say(channel, 'fesses');
    }
};