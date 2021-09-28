#!/bin/bash
# Check if current branch contents has been pushed
if [ -n "$(git status --porcelain)" ]; then
    echo "Check git status; needs commit"
    exit 1
fi
$(git merge-base --is-ancestor @{u} HEAD) || ( \
    echo "Current branch not yet pushed upstream" && exit 2 )
