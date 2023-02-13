# Doc Assetto Speedo

## 🇫🇷 Ton tableau de bord Assetto Corsa pour le web.

Pour faire simple et court, les infos de ta voitures in-game sont rendues dispo sur tout tes appareils. 

Dans une page web sur ton réseau, tu peux y accéder depuis n’importe quel appareil connecté à ton réseau qui sait afficher une page web. 

### Installation (WIP)

1. Place le fichier “AssettoSpeedo.py” dans le dossier “apps” de votre dossier Assetto Corsa. Puis, dans Content Manager, activez l’application depuis la liste des applis.
2. Ligne 40 du fichier .py, modifiez le chemin afin qu’il pointe vers l’emplacement ou vous avez sauvegardé le reste des fichiers. Example :

```jsx
outfile = open( "C:/Utilisateurs/saucisse/Documents/" +"AssettoSpeedo/car_data.json", "w")
```

1. Lancez un serveur web (en utilisant l’extension Live Server dans VSCode par exemple), et assurez vous que le fichier .json est bien en ligne en vous rendant à l’adresse suivante [http://127.0.0.1/car_data.json](http://127.0.0.1/car_data.json). Si vous arrivez bien sur le contenu du fichier c’est tout bon.
2. Votre tableau de bord est dispo sur tout votre réseau, il suffit d’entrer l’IP de votre hôte dans n’importe quel navigateur. 






## **🇬🇧 Your Assetto Corsa dashboard on the web.**

To make it short, you can use this to access your car data from outside the game, on all your devices.

Available on your local network, you can access it from any device able to display a webpage.

### Setup (WIP)

1. Put the “AssettoSpeedo.py” file in your “apps” folder, then enable the app in your Content Manager settings.
2. Line 40 of the .py file, change the path to the location you saved your folder. Example : 

```jsx
outfile = open( "C:/Users/sausage/Documents/" +"AssettoSpeedo/car_data.json", "w")
```

1. Launch a web server (using Live Server exention in VSCode for example) and make sure that the .json file is served by browsing to [http://127.0.0.1/car_data.json](http://127.0.0.1/car_data.json) and making sure data shows up.

### ☄Demo

![GIF de démo](demo.gif)

### TODO

- [ ]  Guide d’installation
- [ ]  Ajout Fuel
- [ ]  Temps ?
- [ ]  Ajout d’un panneau drift optionnel ?
