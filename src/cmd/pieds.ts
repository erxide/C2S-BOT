import tmi from 'tmi.js';
import type { Config } from '../types';

export const pieds_cmd = (BOT:tmi.Client, channel:string, author:string, config:Config) => {
    console.log(`CMD : ${author} a utilisé la cmd pieds`);
    if (config.ADMIN.includes(author) || config.PRENIUM.includes(author)) {
        BOT.say(channel, '⠀⠀⠀⢀⡤⣾⠉⠑⡄⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⣧⢤⡀⠀⠀⠀\n\
⠀⢀⣔⠙⡄⠈⡆⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠀⢠⠃⢠⠋⣢⡀⠀\n\
⣀⣌⠈⡆⣗⣚⠯⠚⠘⢆⠀⠀⠀⠀⠀⠀⡰⠃⠓⠽⣓⣺⢰⡁⣱⣀\n\
⡇⢈⣝⠖⠉⣿⠀⠀⠀⠀⢇⠀⠀⠀⠀⡰⠀⠀⠀⠀⢸⠉⠲⡏⡁⢨\n\
⠘⡺⠁⠀⠀⢸⠀⠀⠀⠀⢸⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢉⡇\n\
⢸⠀⠀⠀⠀⢄⠀⠀⠀⠀⡎⠀⠀⠀⠀⠹⡀⠀⠀⠀⡰⠀⠀⠀⠀⡇\n\
⠈⡄⠀⠀⠀⠘⠄⠀⢀⡜⠀⠀⠀⠀⠀⠀⢣⡀⠀⠠⠃⠀⠀⠀⢠⠃\n\
⠀⠘⡄⠀⠀⠀⠈⠠⠎⡇⠀⠀⠀⠀⠀⠀⢸⠱⠀⠁⠀⠀⠀⢠⠃⠀\n\
⠀⠀⠘⡄⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⢸⠐⠀⠀⠀⠀⢠⠇⠀⠀\n\
⠀⠀⠀⠘⡀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⢀⠆⠀⠀⠀\n\
⠀⠀⠀⠀⢡⠀⠀⠀⠀⠀⠈⡄⠀⠀⢠⠃⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠸⠀⠀⠆⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⢀⠆⠀⡀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀\n\
⠀⠀⠀⠀⠀⠀⠳⠄⣀⣀⠤⠊⠀⠀⠑⠤⣀⣀⠠⠜⠀');
    }
};