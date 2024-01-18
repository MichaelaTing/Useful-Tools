# Git Tutorial

## Configuration

```shell
git config --global user.name xxx
git config --global user.email xxx
git config --global user.password xxx # Here you can set the token through "Github/Settings/Developer Settings"
git config --global http.proxy xxx.xxx.xxx.xxx:zz # Proxy server address: Proxy server port number
git config --list # View information
git config --global --edit # Edit
git config --global credential.helper store # Avoid entering username and password every time `git clone`
```

## Bind Git and GitHub using SSH

```shell
ssh-keygen -t rsa # Generate public and private keys
cd ~/.ssh
cat id_rsa.pub # Add the contents of the public key `id_rsa.pub` in the ~/.ssh folder to "GitHub/Settings/SSH"
ssh -T git@github.com # Test if the binding is successful. If port 22 fails, use port 443 and add the following to ~/.ssh/config:
"
Host github.com
    Hostname ssh.github.com
    Port 443
"
```

## Create a Repository

### Initialize a Repository

```shell
mkdir foldname # Create a folder
cd foldname/
git init # When executing `git init`, Git will create the master/main branch by default.
ls -a
```

### Clone a Remote Repository

```shell
git clone [url]
```

## Commit and Modify

### Add Files to the Staging Area

After modifying a file, you generally need to perform the `git add` operation to save the historical version.

```shell
touch filename # Create a file
git add <file1> <file2>
git add . # Add all unstaged files in the folder at once
```

### View the Status of the Repository, Display Modified Files

```shell
git status # View the status of the repository
git status -s # Abbreviated mode
```

### Commit the Staging Area to the Local Repository

```shell
git commit -m [message]
git commit <file1> <file2> ... -m [message]
git commit -a # Submit changes without executing `git add` after modifying files
```

### Compare the Staging Area and the Working Directory

```shell
git diff # Show unstaged changes
git diff --cached # View cached changes
git diff HEAD # View all changes, both staged and unstaged
git diff --stat # Show summary instead of the whole diff
```

### Revert to Previous Version

```shell
git reset [--soft | --mixed | --hard] [HEAD] # --soft: revert to a certain version; --hard: undo all uncommitted changes in the working directory and staging area, revert both the staging area and the working directory to the previous version, delete all previous information, use with CAUTION!; --mixed: default and can be omitted, HEAD^[n]: n versions before the current version.
```

### Remove Files from the Staging Area and Working Directory

```shell
git rm <file> # Remove file from the staging area and working directory
git rm -r <fold> # Delete local folder
git rm --cached <file> # Remove from the staging area only
git rm –r * # Recursively delete all subdirectories and files in the directory
```
 
### Move or Rename Working Directory Files

```shell
git mv <file> <newfile> # Move or rename file or directory
git mv -f <file> <newfile> # Rename even if the new file name already exists
```

### Tags

```shell
git tag -a v1.0
git tag # View all tags
```

### View the Commit History

```shell
git log # View the commit history
git log --oneline # View a concise version of the commit history
git log --oneline --graph # Enable the topology option
git log --reverse --oneline # Display the log in reverse order
git log --decorate ## View tags
git log --help # View help command
git blame <file> # View the historical modification records of the specified file in a list format.
```

## Branch Management
Almost every version control system supports branches in some form. A branch represents an independent line of development.

Using branches means you can separate from the main development line and continue working without affecting the main line.

Some people call Git's branching model a killer feature, and it is precisely because of this feature that Git stands out from other version control systems.

Adding or deleting files in a branch does not affect the main branch. Using branches separates work and allows us to work in different development environments and switch back and forth.

### Branch

```shell
git branch # View the branches in the Git repository
git branch -a # View the branches in the remote repository
git log --oneline --graph # View the branches
gitbranch <branch-name> # Create new branch
git checkout <branch-name> # Switch to the specified branch
git checkout -b <branch-name> # Create and switch to new branch
git branch -d <branch-name> # Delete branch
```

### Merge Branch
When merging branches, conflicts may occur if the same lines of code have been modified in both branches. Git will mark the conflicts in the affected file, and you need to manually resolve them.

```shell
git merge <branch-name> # Merge the specified branch into the current branch
git merge --no-ff <branch-name> # Perform a non-fast-forward merge, which creates a new commit even if it is a fast-forward merge
```

## Remote Operations

### Remote Repository Operations

```shell
git remote # List the configured remote repositories in the current repository
git remote -v # List the configured remote repositories in the current repository and display their URLs
git remote show <remote_name> # Display detailed information about remote repository
git remote add <remote_name> <remote_url> # Specify a name and URL for a remote repository and add it to the current repository
git remote rename <old_name> <new_name> # Rename remote repository
git remote set-url <remote_name> <new_url> # Modify the URL of remote repository
git remote remove <remote_name> # Remove remote repository from the current repository
git remote rm <remote_name>  # Remove a remote repository
```

### Fetch a Remote Codebase

```shell
git fetch origin # Fetch updated data
git merge origin/master # Synchronize the updates to the local repository
```

### Download and Merge Remote Code

```shell
git pull <remote_hostname> <remote_branch_name>:<local_branch_name>
git pull origin master # Retrieve the master branch from origin and merge it with the local master branch
git pull origin master:brantest # Retrieve the master branch from origin and merge it with the local brantest branch
```

### Upload and Merge Remote Code

```shell
git push <remote_hostname> <local_branch_name>:<remote_branch_name>
git push origin master # Push the local master branch to the master branch of the origin host
git push --force origin master # There are differences between the local and remote versions, but still force the push
git push origin --delete master # Delete the master branch of the origin host
```