# TAILSCALE

Pour mettre en place la connexion entre les machines virtuelle,

Il faut installer l’application Tailscale :https://tailscale.com/download.

Sur les machines hôtes (pour accéder aux différentes machines en ssh) : Téléchargement par l’app store

Sur les machines virtuelles : 

les machines virtuelles utilisent la connexion bridged.

lancer les commandes
```bash
sudo apt install curl
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```
