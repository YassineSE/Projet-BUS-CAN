# Guide de gestion de 'repo git' et commandes utiles.

## 1. Rajouter le git sur votre machine

> Avant tout, assurez-vous d'avoir git installé sur votre machine. 
> Si c'est fait vous pouvez lancer un terminal: Cmd,Powershell,Git Terminal (Windows), Terminal/bash (Linux)

Lancez ces commandes une-à-une
```sh
    git init
    git remote add origin https://github.com/YassineSE/Projet-BUS-CAN.git
    git fetch --all 
    git pull origin main
```

## 2. Credentials et Enregistrement des données sur Terminal
Normalement, à chaque push, le git vous demande de vous indentifier. Même si vous tapez votre mot de passe git, cela ne marchera pas.

Il faut ainsi créer un "personal token" pour pouvoir contribuer sur le repo.

* Allez dans **Settings** puis **Developer settings**.
* Puis dans **Personal Access Tokens** ensuite **Tokens(classic)**
* Enfin cliquez sur: **Generate New Token**

> N.B: Stockez le token dans un fichier dans un endroit sûr de votre machine. 

Maintenant, pour éviter de taper vos coordonnées à chaque push:
* Vous devez taper cette commande
```sh
    git config --global credential.helper store
```

Puis faites votre push normalement (voir partie 3)

## 3. Pull, Push, Merge

Avant tout lancez cette commande
```sh
    git fetch --all
```

> Le projet comporte deux branches principales:
> La branche **dev**: où tout le code va être développé et testé. Dès que cela fonctionne, il faut merge avec la branche main.
> La branche **main**: où se situera le projet final et les parties qui fonctionnent du code. N.B: NE PAS DEVELOPPER DIRECTEMENT SUR CETTE BRANCHE !


### La démarche de développement à suivre:

Dès que vous venez de tester votre code.

```sh
    git branch -M dev
    git add .
```

Puis
```sh
    git commit -m "Un message descriptif..."
```

et finalement:
```sh
    git push origin dev
```

Dès que votre travail est validé par les autres: 
```sh
    git branch -M main
    git merge origin/dev
```