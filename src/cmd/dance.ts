import tmi from 'tmi.js';
import type { Config } from '../types';

export const dance_cmd = (BOT:tmi.Client, channel:string, author:string, config:Config) => {
    console.log(`CMD : ${author} a utilisé la cmd dance`);
    if (config.ADMIN.includes(author) || config.PRENIUM.includes(author)) {
        BOT.say(channel, 'DinoDance '.repeat(10).trim());
    }
};