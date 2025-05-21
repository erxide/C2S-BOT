import tmi from 'tmi.js';

const reactions = [
        "fais la fou avec nous @WizeBot",
        "ntm la pute @WizeBot",
        "ftg @WizeBot",
        "reste a ta place @WizeBot",
        "@WizeBot t'es tellement con que t'es arrivé 3eme a un concours de circonstances",
        "@WizeBot t'as une tete a savoir quel feutre à le meilleur gout",
        "@WizeBot Fais moins l’malin, t’es juste une commande avec du Wi-Fi",
        "@WizeBot t’es comme un interrupteur cassé : t’allumes personne.",
        "@WizeBot Reste à ta place, la dernière fois que t’as servi, c’était pour muter ta propre mère.",
        "@WizeBot t’as un flow de tableau Excel et une âme de captcha.",
        "@WizeBot T’es même pas un vrai bot, t’es un Google Doc qui parle mal.",
        "@WizeBot, si l’intelligence artificielle te regarde, elle pleure.",
        "@WizeBot T’as le charisme d’un code QR moisi sur une porte de chiottes.",
        "@WizeBot, t’es le genre de bot qui perd un débat contre un grille-pain.",
        "@WizeBot T’es utile comme un parapluie dans une tornade numérique.",
        "@WizeBot t’as une voix qui donne envie d’éteindre le son sur un stream muet.",
        "@WizeBot T’as une tête à croire que les cookies sont vraiment faits au chocolat.",
        "@WizeBot, t’es le seul bot qui peut crasher en mode maintenance mentale.",
        "@WizeBot T’as été codé avec les pieds d’un dev en burn-out.",
        "@WizeBot t’es tellement naze que même Nightbot t’a bloqué.",
        "@WizeBot t’a codé un jour férié, avoue."

    ]

export const wizebot_react = (BOT:tmi.Client, channel:string) => {
    BOT.say(channel, `${reactions[Math.floor(Math.random() * reactions.length)]}`)
}