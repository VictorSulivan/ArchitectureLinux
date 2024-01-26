Techno: Postgresql

Caractéristique de la machine:

- Ip: **100.117.30.25**
- Nom de user: database
- Password: database
- Nom de machine sur Tailscale: database
- Nom de l’utilisateur postgres : database / mdp : database
- Nom de la base de données : linux_database

Initialisation de la machine : 

- Création de la machine virtuelle avec serveur ssh

```bash
sudo apt install gnupg2 wget
sudo apt install lsb-release
Repository postgresql : sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt install curl
Repository signing key : curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
Installer postgresql16 : sudo apt install postgresql-16 postgresql-contrib-16
Démarrer postgresql service : sudo systemctl start postgresql
Autoriser postgresql service : sudo systemctl enable postgresql
```

Edit /etc/postgresql/16/main/postgresql.conf : 

listen_addresses = ‘*’ pour autoriser les connexions extérieures

Ajout de l’authentification md5 pour pouvoir connecter depuis l’extérieur

```bash
sudo sed -i '/^host/s/ident/md5/' /etc/postgresql/16/main/pg_hba.conf
sudo sed -i '/^local/s/peer/trust/' /etc/postgresql/16/main/pg_hba.conf
```

Pour appliquer les changements

`sudo systemctl restart postgresql`

Pour autoriser le port postgres à travers le firewall

`sudo ufw allow 5432/tcp`

Connexion à postgresql

`sudo -u postgres psql`

Création de l’utilisateur : 
`CREATE USER database WITH PASSWORD 'database';`

Création de la base de données : 

`CREATE DATABASE linux_database;`

Import du fichier de la base de données depuis la machine hôte :

`scp LINUX_DATABASE.pgsql [database@10.160.33.155](mailto:database@10.160.33.155):/home/database/database_files`

Import de la base de données dans postgres : 
`psql -h localhost -U database -d linux_database -f database_files/LINUX_DATABASE.pgsql`

On peut se connecter à la base depuis la vm avec :

`psql linux_database`

Pour se connecter à Tailscale et être relié aux autres machines : 
`sudo apt install curl`

`curl -fsSL https://tailscale.com/install.sh | sh`

`sudo tailscale up` 

[Lien tailscale](https://login.tailscale.com/admin/machines/100.117.30.25)