googleappengine-djangae-skeleton
================================

**NOTE: potato has released djangae-scaffold (https://github.com/potatolondon/djangae-scaffold), I recommend to use that instead**

A skeleton for building Django applications on Google App Engine using Djangae (https://github.com/lukebpotato/djangae)

It's currently deployed at http://djangae-skeleton.appspot.com/

The project is still in development, check out TODO.md

Install
-------

```
# Install the Google App Engine Python SDK, example:
cd
wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.11.zip
unzip google_appengine_1.9.11.zip
rm google_appengine_1.9.11.zip
export PATH=$PATH:~/google_appengine/

# Clone this repo
git clone https://github.com/davide-ceretti/googleappengine-djangae-skeleton

# Install requirements
cd googleappengine-djangae-skeleton
pip install -r requirements.txt -t lib
```

Run server
----------

```
./run.sh
# App is served at http://localhost:8080/
# Admin interface is served at http://localhost:8000
```

Run tests
---------

```
./test.sh
```

Deploy
------

* Use the Admin Console to create a project/app id. (App id and project id are identical)
* Update app.yaml with the chosen app id
* ```./deploy.sh```

Open shell
----------

```
# Remote
./shell_remote.sh

# Local
./shell.sh
```
