# Day 1 : Setting up foundation

Task:

Create a new folder called task-tracker.
Initialize a Git repository (git init).
Add a README.md with a project description and a basic script (e.g., tracker.py or index.js) that prints "Task Tracker v1.0".
Stage and commit the changes (git add ., git commit -m "Initial commit with README and basic script").
Outcome: A local Git repo with a basic starting point.
Take-Home Check: Verify the commit history with git log

```python
# tracker.py
def main():
    print("Task Tracker v1.0")
    print("Available commands: add, view, update, delete, exit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Command '{command}' not implemented yet.")

if __name__ == "__main__":
    main()
```

```markdown
# Readme.md

# Task Tracker
A simple command-line tool to manage tasks.

## Setup
1. Install Python 3.x.
2. Run `python tracker.py` to start the app.

## Usage
- Type commands: `add`, `view`, `update`, `delete`, or `exit`.
```
Steps:

Create a folder: mkdir task-tracker && cd task-tracker.
Initialize Git: git init.
Create tracker.py and README.md with the code above.
Stage and commit:

```bash
git add .
git commit -m "Initial commit with README and basic script"

```

# Day 2 : Branching for features

Task:

Create a branch called feature/add-task (git branch feature/add-task, git checkout feature/add-task).
Implement a function to add tasks (e.g., store tasks in a list or file).
Commit the changes (git commit -m "Add task creation functionality").
Switch back to main (git checkout main) and merge the branch (git merge feature/add-task).
Simulate a merge conflict: Create another branch feature/edit-readme, modify README.md, merge it, then merge feature/add-task again to resolve a conflict.
Outcome: A repo with a working "add task" feature and experience resolving conflicts.
Take-Home Check: Ensure main has the merged feature and no conflicts

```python

# tracker.py
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

def main():
    print("Task Tracker v1.0")
    print("Available commands: add, view, update, delete, exit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Command '{command}' not implemented yet.")

if __name__ == "__main__":
    main()
```

steps:

1. create feature branch
```bash
git branch feature/add-task
git checkout feature/add-task
```

2. Update tracker.py with the code above.

3. comnit chanages

```bash
git add tracker.py
git commit -m "Add task creation functionality"
```

4. Switch to main and merge

```bash
git checkout main
git merge feature/add-task
```

5. Simulate merge conflict

```
Create a branch feature/edit-readme: git checkout -b feature/edit-readme.
Edit README.md (e.g., add "Version: 1.0").
Commit: git add . && git commit -m "Update README".
Merge to main: git checkout main && git merge feature/edit-readme.
Edit README.md again on feature/add-task (same line), commit, and merge into main to cause a conflict. Resolve it manually and commit.
```
# Day 3 : Pushing to Github 

Task:

Create a new repository on GitHub called task-tracker.
Link the local repo to GitHub (git remote add origin <repo-url>).
Push the main branch (git push -u origin main).
Create a .gitignore file to exclude unnecessary files (e.g., __pycache__, node_modules).
Clone the repo to a new folder (git clone <repo-url>), make a small change (e.g., update README.md), and push it back.
Outcome: A GitHub-hosted project with remote collaboration enabled.
Take-Home Check: Confirm the repo is live on GitHub and changes are synced.

1. create `.gitignore` file

```bash
# .gitignore
__pycache__/
*.pyc
```

2. Commit it: git add .gitignore && git commit -m "Add .gitignore".
3. Create a GitHub repo named task-tracker (public, no README).
4. link and push
```bash
git remote add origin <your-repo-url>
git push -u origin main
```

5. Clone elsewhere

```bash
cd .. && git clone <your-repo-url> task-tracker-clone
cd task-tracker-clone
echo "Test clone" >> README.md
git add . && git commit -m "Test clone" && git push
```
# Day 4: collaborative with pull request

Task:

Fork the task-tracker repo to your own GitHub account (or use a second account).
Clone the forked repo locally.
Create a branch feature/view-tasks and implement a function to display all tasks.
Push the branch to your fork (git push origin feature/view-tasks).
Open a Pull Request from the fork to the original repo, adding a detailed description.
On the original repo, review and merge the PR.
Bonus: Create an Issue on GitHub (e.g., "Add task deletion feature") and link it to a future PR.
Outcome: Experience with collaborative workflows and PRs.
Take-Home Check: Verify the PR is merged and the "view tasks" feature works on main.

```python
# tracker.py
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks yet.")
    except FileNotFoundError:
        print("No tasks yet.")

def main():
    print("Task Tracker v1.0")
    print("Available commands: add, view, update, delete, exit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "view":
            view_tasks()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Command '{command}' not implemented yet.")

if __name__ == "__main__":
    main()
```

Steps:

Fork the repo on GitHub to your account.
Clone the fork: git clone <fork-url> task-tracker-fork.
Create a branch: cd task-tracker-fork && git checkout -b feature/view-tasks.
Update tracker.py with the code above.

commit and push :

```bash
git add tracker.py
git commit -m "Add view tasks functionality"
git push origin feature/view-tasks
```
Open a PR from feature/view-tasks (fork) to main (original repo).
On the original repo, review and merge the PR. Pull changes locally: git pull.
Outcome: "View tasks" is added via collaboration.


# Day 5: Fixing mistakes and rewriting histories

Task:

Create a branch feature/update-tasks and add a task update function with multiple messy commits (e.g., "WIP", "Fix typo", "Add logic").
Squash these into one commit using git rebase -i HEAD~3 (replace 3 with the number of commits).
Push the branch, then realize a mistake (e.g., wrong feature name). Use git revert to undo the last commit on main after merging.
Bonus: Use git reset --soft HEAD^ to undo a commit locally and recommit with a better message.
Outcome: Cleaner history and confidence in fixing mistakes.
Take-Home Check: Ensure the branch history is tidy and the revert worked.

```python
# tracker.py (partial update for brevity)
def update_task(task_num, new_task):
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1] = new_task + "\n"
            with open("tasks.txt", "w") as f:
                f.writelines(tasks)
            print(f"Updated task {task_num} to: {new_task}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to update.")

# Add to main():
elif command == "update":
    view_tasks()
    task_num = int(input("Enter task number to update: "))
    new_task = input("Enter new task: ")
    update_task(task_num, new_task)
```

Steps :

Create a branch: git checkout -b feature/update-tasks.
Add update_task and update main() with messy commits

```bash
git add tracker.py && git commit -m "WIP update"
echo "# Test" >> README.md && git add . && git commit -m "Fix typo"
git add tracker.py && git commit -m "Finish update"
```

Squash commits: git rebase -i HEAD~3, change pick to squash for the last two, save, and edit the message to "Add update tasks functionality".
Merge to main: git checkout main && git merge feature/update-tasks.
Revert a mistake: git revert HEAD (undo the merge), then re-merge correctly.


# Day 6: DevoPs workflow and Automation

Task:

Adopt GitHub Flow: Create a branch feature/delete-tasks, implement task deletion, and open a PR to main.
Add a simple Git hook (e.g., pre-commit script to check for a valid commit message).
Set up a GitHub Action:
Create a .github/workflows/ci.yml file.
Add a basic workflow to run a linter or test (e.g., flake8 for Python, eslint for JS) on every push/PR.
Merge the PR after the Action passes.
Outcome: A DevOps-ready project with automation.
Take-Home Check: Confirm the Action runs successfully and the delete feature works.

```python
# tracker.py (partial update)
def delete_task(task_num):
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if 0 < task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as f:
                f.writelines(tasks)
            print(f"Deleted task: {deleted.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks to delete.")

# Add to main():
elif command == "delete":
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    delete_task(task_num)
```
Steps:

Create a branch: git checkout -b feature/delete-tasks.
Update tracker.py with the code above.
Commit and push: git add . && git commit -m "Add delete tasks" && git push origin feature/delete-tasks.
Open a PR to main.
Add the GitHub Action file, commit, and push. Merge the PR after the CI passes.

# Day 7: Advanced techniques and polish

Tasks :

Use git stash: Start a new feature (e.g., task priority), stash it midway, switch to fix a bug on main, then apply the stash (git stash pop).
Cherry-pick a commit: Create a branch with experimental changes, commit something useful (e.g., a help menu), then use git cherry-pick <commit-hash> to bring it to main.
Recover a deleted branch: Delete feature/delete-tasks after merging, then recover it using git reflog and git branch feature/delete-tasks <hash>.
Add a Git alias (e.g., git config --global alias.cm "commit -m") and use it.
Bonus: Add large files (e.g., a sample task database) with Git LFS.
Outcome: A polished Task Tracker with advanced Git mastery.
Take-Home Check: Test all features (add, view, update, delete tasks) and verify recovery works.

steps:

1. stash : start a priority feature stash it

```
git checkout -b feature/priority
echo "Priority WIP" >> tracker.py
git add . && git stash
```

2. cherry pick

Create a branch experiment, add a help function, commit, then cherry-pick to main:

```bash
git checkout -b experiment
# Add help function (e.g., print commands)
git add . && git commit -m "Add help"
git checkout main
git cherry-pick <commit-hash>
```

Recover a branch: Delete feature/delete-tasks (git branch -d feature/delete-tasks), recover with git reflog and git branch feature/delete-tasks <hash>.

Alias: git config --global alias.cm "commit -m", use it: git cm "Final polish".

