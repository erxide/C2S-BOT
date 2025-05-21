import tmi from 'tmi.js';
import type { Config } from '../types';
import { writeConfig } from '../utils/writeConfig';

export const addPr_cmd = async (BOT:tmi.Client, channel:string, author:string, config:Config, configPath:URL, user:string):Promise<Config> => {
    console.log(`CMD : ${author} a utilisé la cmd addPr`);
    if (user.startsWith('@')) {
        user = user.slice(1);
    }
    if (config.PRENIUM.includes(user)) {
        BOT.say(channel, `@${user} est deja PRENIUM !`);
        return config;
    }
    if (config.ADMIN.includes(author)) {
        config.PRENIUM.push(user);
        const newConfig = await writeConfig(configPath, config);
        BOT.say(channel, `@${user} est maintenan PRENIUM !`);
        return newConfig;
    }
    return config;
};