git init is to start the Git Repo.

git add is for adding the files you want to later commit into your local repo. it´s like saying, hey git, add this into the folder i´ll later push into the remote (GitHub) repo.

git branch is a way into creating the first branch into our repo. -M is to rename. -m is to add a message

git commit is for getting everything in the delivery pack. in here we normally add a -m message to specify the changes that were done.

git push is to actually upload whatever you commited into the remote repo (GitHub) its the final stage you have before actually sending anythin. -u is of upstream and it is used at the beginning to keep uploading files to the same branch (In this case we stated was main)

git remote add origin https://github.com/eduant2607/Random_Projects.git That is for creating the  remote add (origin) that is the alias of the whole URL we see up. Can be anything but origin is mainly used

git init
git remote add origin <repository_url>
git branch -M main
git add .
git commit -m 'Your commit message here!'
git status
git push -u origin main

This would be the typical flow of action into ceating a new repo!

