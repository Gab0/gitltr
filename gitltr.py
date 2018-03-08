#!/bin/python

import git

GIT = git.cmd.Git('.')
repo = git.Repo('.')
files = GIT.ls_files()

Q=repo.index.diff(repo.head.commit)
C=repo.index.diff('HEAD')
N=repo.head.commit.diff()

FileDiffs = repo.index.diff(None)

DIFFS = repo.git.diff(repo.head.commit.tree)
#print(DIFFS)

for F in FileDiffs:
    File = F.b_path
    commitsOnFile = list(repo.iter_commits(paths=File))
    print("Changes for %s:" % File)

    latestCommit = commitsOnFile[0]
    print(repo.git.diff(None, latestCommit, File))

    MSG = input("Commit message for %s:\n" % File)

    repo.index.add([File])
    repo.index.commit(MSG)
