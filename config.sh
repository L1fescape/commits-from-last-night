#!/bin/bash

info () {
  printf "  [ \033[00;34m..\033[0m ] $1"
}

user () {
  printf "\r  [ \033[0;33m?\033[0m ] $1 "
}

success () {
  printf "\r\033[2K  [ \033[00;32mOK\033[0m ] $1\n"
}


user ' - What is your github username?'
read -e username
user ' - What domain should I post commit messages to? '
read -r url

sed -e "s/GITHUB_USERNAME/$username/g" -e "s/DOMAIN_URL/$url/g" templates/post-commit.tmpl > hooks/post-commit

success "Successfully created 'hooks/post-commit'. Yisss."


FLASK_DOMAIN=localhost
FLASK_PORT=5000
MONGO_DOMAIN=localhost
MONGO_PORT=27017

sed -e "s/FLASK_DOMAIN/$FLASK_DOMAIN/g" -e "s/FLASK_PORT/$FLASK_PORT/g" -e "s/MONGO_DOMAIN/$MONGO_DOMAIN/g" -e \
"s/MONGO_PORT/$MONGO_PORT/g" templates/settings.py.tmpl > server/settings.py

success "Successfully created 'server/settings.py'. Bam."

info "Fin. \n"
