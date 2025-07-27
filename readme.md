# Installation

## python umgebung erstellen
* nur 1x notwendig!

python -m venv .venv 

## python umgebung aktivieren
* immer notwendig, ob aktiv sieht man an der eingabeaufforderung, vorne steht dann: "(.venv)" 

source .venv/bin/activate

## streamlit installieren
* nur einmal notwendig

pip install streamlit

## programm ausführen
* statt app.py kann jeds streamlit programm ausgeführt werden

streamlit run app.py

# GIT

# Docker 

https://docs.streamlit.io/deploy/tutorials/docker#install-docker-engine

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04#step-3-using-the-docker-command

docker push registry.digitalocean.com/shadowframe/space

docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname

### auth!
https://www.digitalocean.com/community/questions/unable-to-push-to-container-registry

### for strato / plesk
docker save -o ~/Downloads/images/space.tar space

## build the container

docker build -t space .

## List running Images or Images

docker images

docker ps

## Docker Administration

docker container ls -a
docker image ls
docker container rm <container_id>
docker image rm <image_id>

### Killt alles !!!!
docker system prune -a

## run the container

docker run -p 80:80 app

docker run -d -p 80:80 space


