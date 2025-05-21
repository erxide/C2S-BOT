import tmi from 'tmi.js';
import type { Config } from '../types';
import { writeConfig } from '../utils/writeConfig';

export const rmPr_cmd = async (BOT:tmi.Client, channel:string, author:string, config:Config, configPath:URL, user:string):Promise<Config> => {
    console.log(`CMD : ${author} a utilisé la cmd rmPr`);
    if (user.startsWith('@')) {
        user = user.slice(1);
    }
    if (!config.PRENIUM.includes(user)) {
        BOT.say(channel, `@${user} est pas PRENIUM !`);
        return config;
    }
    if (config.ADMIN.includes(author)) {
        config.PRENIUM = config.PRENIUM.filter(u => u !== user);
        const newConfig = await writeConfig(configPath, config);
        BOT.say(channel, `@${user} n'est plus PRENIUM !`);
        return newConfig;
    }
    return config;
};