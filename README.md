# SyncGit
Sync two git repo in one local code

The local folder structure maybe:

.git<br/>
.git_right<br/>
.gitingore<br/>
Code

and then:

.git_left<br/>
.git<br/>
.gitingore<br/>
Code

last:

.git<br/>
.git_right<br/>
.gitIngore<br/>
Code

The two repo has the same code but only in different remote repo.
the sync script will merge only one commit once.
and then sync this merged change into the right repo by commit.
if current commit complemeted, will get the next commit in the left repo, and then repeat it util the left repo is synced with the right repo.

Request:<br/>
GitPython

WARNING: the args should be:<br/>
argv[0]:sync.py<br/>
argv[1]:git repo local path<br/>
argv[2]:.git name, maybe:.git_left as the source repo<br/>
argv[3]:.git name, maybe:.git_right as the dest repo
