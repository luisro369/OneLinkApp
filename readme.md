# Welcome to the onelink app

This is a test app build in Django designed to Query a postgresql database and be a great CRUD interface for web development.

### Instalation Linux systems


# Postgresql Database 

* Download Postgresql (on local/virtual or container for ubuntu[distro optional])

sudo apt install postgresql postgresql-contrib

* One installed make sure the database is running

systemctl status postgresql

- If not:

systemctl start postgresql

* Configuring Postgresql for accepting connections to other devices (ip's)

sudo vi /etc/postgresql/12/main/pg_hba.conf

- Edit/add the line:

 TYPE  DATABASE        USER            ADDRESS                 METHOD
host    all             postgres        192.168.1.0/24          md5
 "local" is for Unix domain socket connections only

and make sure you put the ip range from which the DB will get it's requests

- Then you need to open up "listen_addresses", you do that by modifying:

sudo vi /etc/postgresql/12/main/postgresql.conf

Search for an uncomment the line:

 CONNECTIONS AND AUTHENTICATION
------------------------------------------------------------------------------

 - Connection Settings -

listen_addresses = '*'           what IP address(es) to listen on;
                                        comma-separated list of addresses;
                                        defaults to 'localhost'; use '*' for >
                                        (change requires restart)
port = 5432                             (change requires restart)
max_connections = 100                   (change requires restart)

- And you are good to go!!! make sure to know the ip of the postgresql server


# Anaconda/Miniconda:

* Download anaconda(optional): https://docs.conda.io/en/latest/miniconda.html
* Install anaconda:

sudo chmod u=rwx ~/File/Path/miniconda.sh

./miniconda.sh

Follow the steps, and you're done!!.


* Create a Django Enviroment:

conda create --name MyEnv django

* Ativate your enviroment:

conda activate MyEnv

* (on Env) Clone this repo and start Django server

git clone https://github.com/luisro369/OneLinkApp.git

python3.x manage.py runserver



##### Requirements
* Python 3.9.7 or greater
* Django 3.2.5
* Anaconda or Miniconda (optional)
* PostgreSQL 12.7 or greater
