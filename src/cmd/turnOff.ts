import tmi from 'tmi.js';
import type { Config } from '../types';

export const turnOff_cmd = (BOT:tmi.Client, channel:string, author:string, config:Config):boolean|undefined => {
    console.log(`CMD : ${author} a utilisé la cmd turnOff`);
    if (config.ADMIN.includes(author)) {
        BOT.say(channel, 'Salut a la prochaine');
        return true;
    }
    return undefined;
};