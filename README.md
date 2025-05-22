# CDEUXS bot TWITCH

Pour installer les dépendances :

```bash
bun install
```

Pour lancer :

```bash
bun run src/index.ts
```

Ce projet a été créé avec `bun init` sous bun v1.2.2. [Bun](https://bun.sh) est un runtime JavaScript tout-en-un rapide.

## COMPORTEMENTS :

- répond '@username quoicoubeh' lorsqu'un user tape 'quoi' dans son message 

- répond '@username caca ? comme caca2squidgame mon créateur!' lorsqu'un user tape 'caca' dans son message 

- répond 'fiouuu y'en a des mots là @username'
si un user utilise 30 mots ou plus dans son message

- répond à wizebot avec un message aléatoire désagréable lorsqu'il parle

## CMD :

### NORMIES :

- Pour voir si le bot est up :
    ```txt
    !c2s
    ```
- Pour voir l'url du repo github du bot :
    ```txt
    !repo
    ```
- Pour jouer au jeu de la boule de cristal :
    ```txt
    !boule <votre question>
    ```

### PREMIUMS :

- Pour faire un pavé de creeper :
    ```txt
    !fesses
    ```
- Pour poser une question à chat gpt :
    ```txt
    !gpt <votre question>
    ```
- Pour envoyer un ascii art de pieds :
    ```txt
    !pieds
    ```

### ADMINS :

- Pour mettre en veille le bot :
    ```txt
    !turnOff
    ```
- Pour mettre en fonctionnement le bot :
    ```txt
    !turnOn
    ```
- Pour ajouter un premium :
    ```txt
    !addPr @<username>
    ```
- Pour supprimer un premium :
    ```txt
    !rmPr @<username>
    ```