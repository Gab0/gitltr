#!/bin/python

import git

GIT = git.cmd.Git('.')
repo = git.Repo('.')

FileDiffs = repo.index.diff(None)

DIFFS = repo.git.diff(repo.head.commit.tree)

if not FileDiffs:
    exit("Nothing to do.")

for F in FileDiffs:
    File = F.b_path
    commitsOnFile = list(repo.iter_commits(paths=File))
    print("Changes for %s:" % File)

    latestCommit = commitsOnFile[0]

    try:
        textualDifference = repo.git.diff(None, latestCommit, File)
    except Exception as e:
        print("Skipping non-modifying commit.")
        print(e)
        raise
        continue

    print(textualDifference)

    MSG = input("Commit message for %s:\n" % File)

    repo.index.add([File])
    repo.index.commit(MSG)
