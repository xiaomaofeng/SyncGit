from cgitb import reset
import imp
from urllib import response
import git
import sys
import re
import os
from git import Repo

def get_last_commit_hash(log, message):
	logs = log.split('\n')
	if len(logs) > 0:
		currentLog = logs[len(logs) - 1]
		res = re.match('^[0-9a-zA-Z](.+?)(?=\s)', currentLog)
		if res != None:
			message[0] = currentLog[len(res.group(0)) + 1:]
			return res.group(0)

	return ""

def fetch_code(message):
	res = True
	repository = Repo.init(sys.argv[1])
	#repository.git.clean('-fd')
	repository.git.reset('--hard')
	repository.git.fetch()
	log = repository.git.log('head..fetch_head', '--first-parent','master', '--oneline')
	commit = ""
	if len(log) > 0:
		commit = get_last_commit_hash(log, message)
	else:
		res = False

	if commit != "":
		repository.git.merge(commit)
	else:
		res = False

	repository.close()
	return res

def commit_code(message):
	repository = Repo.init(sys.argv[1])
	log = repository.git.log()
	repository.git.pull()
	repository.git.add('-A')
	repository.git.commit('-a', '-m', message)
	repository.git.push()	
	repository.close()

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Please input repo local directory and repo .git folder name")
		sys.exit()
	
repo_left = sys.argv[1] + sys.argv[2]
repo_right = sys.argv[1] + sys.argv[3]
repo_name = sys.argv[1] + ".git"
if not os.path.exists(repo_right):
	os.rename(repo_name, repo_right)
	os.rename(repo_left, repo_name)
message = [""]
while(fetch_code(message)):

	if not os.path.exists(repo_left):
		os.rename(repo_name, repo_left)
		os.rename(repo_right, repo_name)
	if message[0] != "":
		commit_code(message[0])

	if not os.path.exists(repo_right):
		os.rename(repo_name, repo_right)
		os.rename(repo_left, repo_name)
