import tmi from 'tmi.js';

const BOT = new tmi.Client({
    identity: {
        username: 'cdeuxs',
        password: process.env.TWITCH_TOKEN
    },
    channels : ['dhalsiiim']
});

BOT.connect();

BOT.on('connected', () => {
    console.log(`✅ Bot ${BOT.getUsername()} connecté à Twitch !`);
})