import tmi from 'tmi.js';
import { c2s_cmd } from './cmd/c2s';
import { repo_cmd } from './cmd/repo';
import { boule_cmd } from './cmd/boule';
import { getConfig } from './utils/getConfig';
import type { Config } from './types';
import { fesses_cmd } from './cmd/fesses';
import { addPr_cmd } from './cmd/addPr';
import { rmPr_cmd } from './cmd/rmPr';
import { turnOff_cmd } from './cmd/turnOff';
import { turnOn_cmd } from './cmd/turnOn';
import { gpt_cmd } from './cmd/gpt';
import { wizebot_react } from './react/wizebot';
import { pieds_cmd } from './cmd/pieds';

let turnOff:boolean = false;
const configPath:URL = new URL('../config.json', import.meta.url);
let config:Config = await getConfig(configPath);

const BOT = new tmi.Client({
    identity: {
        username: 'cdeuxs',
        password: process.env.TWITCH_TOKEN
    },
    channels : ['caca2squidgame']
});

BOT.connect();

BOT.on('connected', () => {
    console.log(`✅ Bot ${BOT.getUsername()} connecté à Twitch !`);
});

BOT.on('message', async (channel, tags, message, self) => {
  if (self) return;

  const auteur:string = tags['display-name'] || tags.username || 'anonymous';
  const msg = message.trim();

  if (!msg.startsWith('!') && !turnOff) {

    if (auteur == "wizebot") {
        console.log(`REACTION : ${BOT.getUsername()} a repondu a ${auteur}`);
        wizebot_react(BOT, channel)
    }

    if (msg.toLowerCase().includes('quoi')) {
        console.log(`REACTION : ${BOT.getUsername()} a repondu au quoi de ${auteur}`);
        BOT.say(channel, `@${auteur} quoicoubeh`);
    }

    if (msg.toLowerCase().includes('caca')) {
        console.log(`REACTION : ${BOT.getUsername()} a repondu au caca de ${auteur}`);
        BOT.say(channel, `@${auteur} caca ? comme caca2squidgame mon createur !`);
    }

    if (msg.split(/\s+/).length >= 30) {
        console.log(`REACTION : ${BOT.getUsername()} a repondu au long text de ${auteur}`);
        BOT.say(channel, `fiouuu y'en a des mots la @${auteur} !`);
    }
  }
  
  if (msg.startsWith('!')) {
    const [command, ...args] = msg.slice(1).split(' ');

    switch (command) {

        case 'turnOn':
        turnOff = turnOn_cmd(BOT, channel, auteur, config) ?? turnOff;
        break;

        default:
            if (turnOff) return;

            switch (command) {
                case 'c2s':
                    c2s_cmd(BOT, channel, auteur);
                    break;

                case 'repo':
                    repo_cmd(BOT, channel, auteur);
                    break;

                case 'boule':
                    boule_cmd(BOT, channel, auteur);
                    break;

                case 'fesses':
                    fesses_cmd(BOT, channel, auteur, config);
                    break;
                
                case 'addPr':
                    if (!args[0]) {
                        BOT.say(channel, 'pour ajouter un membre en PRENIUM : !addPr @<username>');
                        break;
                    }
                    config = await addPr_cmd(BOT, channel, auteur, config, configPath, args[0]);
                    break;
                
                case 'rmPr':
                    if (!args[0]) {
                        BOT.say(channel, 'pour enlever un membre de PRENIUM : !rmPr @<username>');
                        break;
                    }
                    config = await rmPr_cmd(BOT, channel, auteur, config, configPath, args[0]);
                    break;

                case 'turnOff':
                    turnOff = turnOff_cmd(BOT, channel, auteur, config) ?? turnOff;
                    break;

                case 'gpt':
                    gpt_cmd(BOT, channel, auteur, config, message);
                    break;

                case 'pieds':
                    pieds_cmd(BOT, channel, auteur);
                    break;

                default:
                    return;
            }
    }
  }
});