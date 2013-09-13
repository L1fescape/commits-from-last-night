# Commits from Last Night
> shit this is a backup in case my computer breaks


## Install

- Install [Mongodb](http://docs.mongodb.org/manual/installation/)
- Run `pip install flask pymongo simplejson`
- Run `sh config.sh` to create config files and git hooks. This will prompt you for your github email, domain to post commit messages to, and mongodb settings. It will also create two files: `hooks/post-commit` and `server/settings.py`.
- Copy newly created `hooks/post-commit` into the `.git/hooks` folder of any repo you'd like this project to track commit messages from.


## Run the Server

Just run this:

```
python server/app.py
```
