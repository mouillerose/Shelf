

Il faut d'abord commencer par créer l'environnement virtuel, deplacez-vous dans le dossier "shelf" du projet, et entrez la commande suivante : 

virtualenv env -p python3

Pour activer l'environnement virtuel entrez la commande 

. env/bin/activate

La première fois que vous activez ce projet, éxécutez les commandes suivante pour installer dans votre environnement les applications requises 

sudo apt update
sudo apt -y upgrade
sudo apt install python3-pip	
pip install -r requirements.txt
   
Dépalcez vous dans le dossier "shelf_project" et activez le serveur avec la commande suivante :

./manage.py runserver

Allez à l'adresse suivante dans votre navigateur web préféré :

127.0.0.1:8000/
