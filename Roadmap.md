
This repository consists of 7 days of Git and Github course in which it covers a to z of git with practical implemenation. We will have task-tracker project for the same


# Day 0: Introduction to Version Control & Git Basics

What is Version Control? (Centralized vs Distributed)
Why Git? Brief history and its importance in modern development.
Installing Git (Windows, macOS, Linux).
Configuring Git: git config (username, email).
Basic Commands:
git init (create a repository).
git add (stage changes).
git commit (save changes).
git status & git log (check repo state).
Hands-on Demo:
Initialize a repo, add a text file, commit changes, and view the log.
Take-Home Exercise:
Install Git on your system.
Create a folder, initialize a Git repo, add a file (e.g., readme.txt), and commit it with a meaningful message.

# Day 1: Working with Git - Branching & Merging 

What are branches? Why use them?
Commands:
git branch (list/create branches).
git checkout (switch branches).
git merge (combine branches).
Hands-on Demo:
Create a feature branch, add a change, merge it back to main.
Simulate a merge conflict and resolve it.
Best Practices: Naming branches, keeping commits small.
Take-Home Exercise:
Create a repo with a main branch.
Make a new branch called dev, add a feature (e.g., a new file), and merge it back to main.
Intentionally create a merge conflict (edit the same line in two branches) and resolve it.



# Day 2: Introduction to GitHub - Remote Repositories

What is GitHub? Difference between Git and GitHub.
Setting up a GitHub account and creating a repository.
Commands:
git remote add origin (link to remote).
git push (upload changes).
git pull (download changes).
git clone (copy a repo).
Hands-on Demo:
Create a GitHub repo, link a local repo, push commits, and clone it elsewhere.
SSH vs HTTPS for authentication.
Take-Home Exercise:
Create a GitHub account (if not already done).
Initialize a local repo, connect it to a new GitHub repo, and push a few commits.
Clone the repo to a different folder and make a change.

 
# Day 3: Collaboration with GitHub - Pull Requests & Issues

Forking vs Cloning: When to use each.
What are Pull Requests (PRs)? Workflow for code review.
Using Issues to track bugs/features.
Commands:
git fetch (get remote updates).
git rebase (optional intro).
Hands-on Demo:
Fork a sample repo, create a branch, make changes, and submit a PR.
Simulate reviewing and merging a PR.
Best Practices: Writing good PR descriptions, commit messages.
Take-Home Exercise:
Fork a public repo (or use your own).
Create a branch, add a small feature, and submit a PR to your own repo.
Bonus: Pair with a friend to review each other’s PRs.


# Day 4: Advanced Git - Undo Changes & History Management

Undoing Changes:
git reset (soft, mixed, hard).
git revert (safe undo).
git checkout -- (discard uncommitted changes).
Rewriting History:
git commit --amend (edit last commit).
git rebase -i (interactive rebase).
Hands-on Demo:
Undo a commit with reset and revert.
Squash multiple commits into one using interactive rebase.
When not to rewrite history (public branches).
Take-Home Exercise:
Create a repo with 5 commits.
Use git reset to remove the last 2 commits, then use git revert to undo another.
Combine 3 commits into 1 using git rebase -i.

# Day 5: Git for DevOps - Workflows & Automation
Popular Git Workflows:
Git Flow (feature, develop, release, hotfix branches).
GitHub Flow (simplified PR-based).
Trunk-based development (brief intro).
Git Hooks: Automating tasks (e.g., pre-commit linting).
GitHub Actions: Intro to CI/CD (build, test, deploy).
Hands-on Demo:
Set up a simple GitHub Flow with a PR.
Add a basic GitHub Action to lint code on push.
Take-Home Exercise:
Create a repo with a main and develop branch following Git Flow.
Add a simple Git hook (e.g., pre-commit to echo a message).
Set up a GitHub Action to print “Hello World” on push (use a template).

# Day 6: Pro Tips & Real-World Scenarios

Advanced Commands:
git stash (save work temporarily).
git cherry-pick (apply specific commits).
git bisect (find bugs in history).
Real-World Scenarios:
Recovering a deleted branch.
Syncing a forked repo with upstream.
Handling large files with Git LFS (brief intro).
Hands-on Demo:
Stash changes, cherry-pick a commit, and recover a branch.
Final Tips: aliases (git co for checkout), .gitignore, team collaboration etiquette.
Take-Home Exercise:
Create a repo, delete a branch, and recover it using git reflog.
Use git stash to save incomplete work, switch branches, then apply the stash.
Bonus: Set up a Git alias (e.g., git st for status).

# Day 7: Interview Preparation
