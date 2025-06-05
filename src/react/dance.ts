import tmi from 'tmi.js';

export const dance_react = (BOT:tmi.Client, channel:string) => {
    BOT.say(channel, 'DinoDance '.repeat(10).trim())
}