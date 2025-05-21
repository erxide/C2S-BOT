import tmi from 'tmi.js';

const reponse:string[] = [
    'Oui, clairement ! 🔮',
    'Non, sûrement pas. ❌',
    'Les astres sont confus... 🤔',
    'Probablement oui ! 🌟',
    'Hmm... c\'est un grand OUI du destin. ✅',
    'Pas pour l’instant, mais persévère ! 💪',
    'C’est écrit dans les étoiles... peut-être 🌠',
];

export const boule_cmd = (BOT:tmi.Client, channel:string, author:string) => {
    console.log(`CMD : ${author} a utilisé la cmd boule`);
    BOT.say(channel, `@${author} ${reponse[Math.floor(Math.random() * reponse.length)]}`);
};