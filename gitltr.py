#!/bin/python

import git

GIT = git.cmd.Git('.')
repo = git.Repo('.')
files = GIT.ls_files()

Q=repo.index.diff(repo.head.commit)
C=repo.index.diff('HEAD')
N=repo.head.commit.diff()

W = repo.index.diff(None)

DIFFS = repo.git.diff(repo.head.commit.tree)
#print(DIFFS)

for F in W:
    File = F.b_path
    AA = list(repo.iter_commits(paths=File))
    print("Changes for %s:" % File)
    LastCommit = AA[-1]
    print(repo.git.diff(None, LastCommit, File))
    MSG = input("Commit message for %s:\n" % File)
    repo.index.add([File])
    repo.index.commit(MSG)
