# Back

Techno:

Caractéristique de la machine:

- Ip: **100.117.174.114**
- Nom de user: backuser
- Password: backuser
- Nom de machine sur Tailscale: backmachine

Lien tailscale: 

[](https://login.tailscale.com/admin/machines/100.117.174.114)

cocher les options durant la création de la machine virtuelle :

- serveur ssh

package à installer :

- python 3.10
- curl (pour Tailscale)
- dotenv
- fastapi

exemple :

```jsx
sudo apt install python3.10

sudo apt-get update
sudo apt-get install curl

pip3.10 install python-dotenv

pip3.10 install fastapi

sudo apt-get update
sudo apt-get install curl
```

ajouter la machine virtuelle à Tailscale:

et suivre les instructions :

```jsx
curl -fsSL https://tailscale.com/install.sh | sh
```

pour démarrer le backend:

```jsx
cd /home/backuser/backend-project/api
python3.10 main.py
```

pour arrêter le backend:

```jsx
control+c
```

pour aller sur les autres machine:
