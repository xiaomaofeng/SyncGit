# SyncGit
Sync two git repo in one local code

The local folder structure maybe:
.git
.git_right
.gitingore
Code

and then:
.git_left
.git
.gitingore
Code

last:
.git
.git_right
.gitIngore
Code

The two repo has the same code but only in different remote repo.
the sync script will merge only one commit once.
and then sync this merged change into the right repo by commit.
if current commit complemeted, will get the next commit in the left repo, and then repeat it util the left repo is synced with the right repo.
