import tmi from 'tmi.js';
import type { Config } from '../types';

export const turnOn_cmd = (BOT:tmi.Client, channel:string, author:string, config:Config):boolean|undefined => {
    console.log(`CMD : ${author} a utilisé la cmd turnOn`);
    if (config.ADMIN.includes(author)) {
        BOT.say(channel, 'Je suis de retour ^^');
        return false;
    }
    return undefined;
};