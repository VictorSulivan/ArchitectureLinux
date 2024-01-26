# Front

Techno : PHP

Caractéristique de la machine :

- Ip: **100.101.103.59**
- Nom d'user : frontend
- Password: root
- Nom de machine sur Tailscale: frontend

Lien Tailscale : 
```bash
https://login.tailscale.com/admin/machines/100.101.103.59
```

cocher les options durant la création de la machine virtuelle :

- serveur ssh
- serveur web

package à installer :

- apache2
- curl (pour Tailscale)

exemple :

```bash
sudo apt install apache2

OU

apt-get install apache2
```

ajoute la machine virtuelle à Tailscale:

et suivre les instructions

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Télécharger le fichier index.php puis l’ajouter dans le dossier “/var/www/html” dans la virtuelle machine.

https://github.com/VictorSulivan/ArchitectureLinux/blob/frontend/index.php

à partir de la machine virtuelle :

```bash
sudo chmod g+w /var/www/html
```

à partir de la machine hôte :

aller dans le dossier avec lequel il y a le fichier index.php

```bash
sudo scp index.php frontend@100.101.103.59:/var/www/html
```

**activer le backend et la BDD avant de démarrer le frontend sinon les requêtes ne marcheront pas**

Démarrer le serveur frontend :

```bash
sudo systemctl start apache2.service
```

puis aller sur le lien :

http://100.101.103.59/index.php

Arrêter le serveur apache :

```bash
sudo systemctl stop apache2.service
```

Redémarrer le serveur :

```bash
sudo systemctl restart apache2.service
```

pour aller sur les autres machines :
```jsx
pour la machine back :
ssh backend@100.117.174.114
mdp:backend

pour la machine base de donnée :
ssh database@100.117.30.25
mdp:database
```
