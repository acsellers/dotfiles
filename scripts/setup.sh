#!/bin/bash
echo 'branching from github'

git checkout master $1
cd $1
git pull
git branch $1
git checkout $1

echo 'copying files to new branch'

cp ~/.gf/database.yml config/database.yml
cp ~/.gf/mongo.yml config/mongo.yml
cp ~/.gf/environment.rb config/environment.rb
cd ~/.gf/.rvmrc .rvmrc

echo rubying

rvm use 1.8.7@gf
powder
