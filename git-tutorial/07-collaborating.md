| [⬅ 6. Setting up a remote repository in GitHub](06-remotes-in-github.md) | [Table of Contents](00-contents.md) | 
| :---- |:----:|

# 7. Collaborating

In section five of this tutorial you learned about branches. You can use branches to collaborate on projects. 

For the next step, get into pairs.  One person will be the "Owner" and the other will be the "Collaborator". The goal is that the Collaborator add changes into the Owner's repository. We will switch roles at the end, so both persons will play Owner and Collaborator.

## Setup access 

The Owner needs to give the Collaborator access. On GitHub, click the settings button on the right,
then select Collaborators, and enter your partner's username.

![Adding Collaborators on GitHub](fig/github-add-collaborators.png)

To accept access to the Owner's repo, the Collaborator needs to go to [https://github.com/notifications](https://github.com/notifications).
Once there she can accept access to the Owner's repo.

## Make copies
Next, the Collaborator needs to download a copy of the Owner's repository to her
 machine. This is called "cloning a repo". To clone the Owner's repo into
her `Desktop` folder (for example), the Collaborator enters:

```
$ git clone https://github.com/vlad/planets.git ~/Desktop/vlad-planets
```

Replace 'vlad' with the Owner's username.

### Protect master
Now both the Collaborator and the Owner have a local copy of the master branch of the repository. However neither of them should make changes to the master, instead they should work on personal branches. To protect the master from getting unreviewed changes, the Owner can protect the master branch. To do this

1. Owner should navigate to the main page of the repository on github.
2. Under the repository name, click Settings.
3. In the left menu, click Branches.
4. Under Branch Protection Rules, select the master branch.
5. Select "Protect this branch" and also "Require pull request reviews before merging", and click Save changes.

## Make changes to a branch
The Collaborator should make a branch of the Collaborator's local master and switch to it

```
git branch wolfman-pluto
git checkout wolfman-pluto
```

The Collaborator can now make a change in her clone of the Owner's repository,
exactly the same way as we've been doing before:

```
$ cd ~/Desktop/vlad-planets
$ vi pluto.txt
$ cat pluto.txt
Co-signers: Wolfman, Dracula, Frankenstein, and Mummy
It is so a planet!
A planet with a heart on its surface; what's not to love?
And hearts have lots of love.
Pluto & Charon are 2 planets orbiting a center of mass outside either one -- no howling at Charon, it's not a moon
```

```
$ git add pluto.txt
$ git commit -m "Fixed order of statements"
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
```


Then push the change to your branch on the *Owner's repository* on GitHub:

```
$ git push origin wolfman-pluto
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 306 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/vlad/planets.git
   9272da5..29aba7c  wolfman-pluto -> wolfman-pluto
```

Take a look to the Owner's repository on its GitHub website now (maybe you need
to refresh your browser.) You should be able to see the new branch made by the
Collaborator.

## Submit a pull request
Now we need to merge the changes. To do this, the Collaborator submits a pull request to the owner. To do this

1. Switch to the new branch (`wolfman-pluto`) in Github.
2. Click on the new pull request.

The Collaborator will then be given a review page that presents an overview of the changes, and a place to write a comment. After filling them in click `Create pull request`.

Now it is the owners job to review the proposed changes. On the owners gitub page, go to the pull requests tab. Click on the new pull request from the contributor to review the suggested changes, add comments if necessary.

Once you are ready to merge you can click `Merge pull request` to merge the branch with master on github. Both the owner and collaborator can now pull the changes from master on github to master in their local copies by entering

```
$ git pull origin master
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/vlad/planets
 * branch            master     -> FETCH_HEAD
Updating 9272da5..29aba7c
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
```

Now the three repositories (Owner's local, Collaborator's local, and Owner's on GitHub) are back in sync.

Since the Owner (vlad) has protected the master branch, in order to modify files the owner should also make a branch, e.g., `vlad-saturn`, and perform a pull request when ready to merge changes into master.

### Switch Roles and Repeat

If time permits, switch Collaborator/Owner and repeat the whole process.

## A Basic Collaborative Workflow

In practice, it is good to be sure that you have an updated version of the
repository you are collaborating on, so you should `git pull` locally before making
any changes. The basic collaborative workflow would be:

* update your local repo with `git pull origin branch-name` for `branch-name=master, my-branch1` or any other branches you are working on.
* locally update your working branch(es) with any new changes from master, *note you don't want to merge into master, but merge master into the branch(es) you have are working on*
    1. `git checkout my-branch1`
    2. `git merge master`
* make your changes\*\* and stage them with `git add`,
* commit your changes with `git commit -m`, and
* upload the changes to GitHub with `git push origin my-branch1`
* once your branch features are complete, submit a pull request

\*\* Frequently interrupt this process to update your master branch from github and merge it into your working branch (`my-branch1`).

### Notes about branches:
1. As all collaborators will have access to all the branches, make sure that your branch names reflect the kinds of changes that you intend to make. 
2. If you have completed working on a branch and have merged all changes to master, you can delete it unless you plan to make further changes to reduce branch clutter (you can see the `delete branch` button at the bottom of successful merged pull requests and delete local copies using `git branch -d branch_name`).
3. Keep as many branches as you need concurrently, but don't forget to make sure they are as up to date as possible with master - this will make it easier to merge any pull requests you submit on github.

### Other notes about collaborating
1. It is better to make many commits with smaller changes rather than
one commit with massive changes: small commits are easier to
read and review.
2. Version control's ability to merge conflicting changes is another reason users tend to divide their programs and papers into multiple files instead of storing everything in one large file. There's another benefit too: whenever there are repeated conflicts in a particular file, the version control system is essentially trying to tell its users that they ought to clarify who's responsible for what, or find a way to divide the work up differently.

Note `git pull` is really equivalent to running `git fetch` and then `git merge`, where `git fetch` updates your so-called "remote tracking branches" and `git merge` combines the two branches that were created locally and remotely (the latter is the "origin" branch in the local system nomenclature).

## Review Changes

The Owner push commits to the repository without giving any information
to the Collaborator. How can the Collaborator find out what has changed with
the command line?

```
git fetch origin
git diff origin master
```

## Comment Changes in GitHub
The Collaborator has some questions about one line change made by the Owner and
has some suggestions to propose.

With GitHub, it is possible to comment the diff record of a commit. Over the line of
code in the diff record, a blue comment icon (+ symbol) appears, which you can click to open a comment window. The Collaborator posts comments and suggestions using the GitHub interface. Now the comment appears as a bubble in the commits summary. Github will also send a notification email about the comment, but sometimes these emails are delayed.

## Reverting a Commit

Jennifer is collaborating on her Python script with her colleagues and
realizes her last commit to the group repository is wrong and wants to
undo it.  Jennifer needs to undo correctly so everyone in the group
repository gets the correct change.  `git revert [first wrong commit ID]`
will make a new commit that undoes Jennifer's previous wrong
commits back to and including that ID. This command affects her local copy, and she can
then git push the changes to GitHub. Note that `git revert` is 
different than `git reset --hard [prior commit ID]` because `reset` literally
goes back to an earlier copy and deletes all subsequent commits, whereas
`revert` undoes all the wrong commits in a new commit so that the history
of wrong commits is retained. The latter is preferable when collaborating. 
Below are the right steps and explanations for Jennifer to use the `git revert` command


1. `git log` # Look at the git history of the project to find the commit ID
2. Copy the ID (the first few characters of the ID, e.g. `0b1d055`).
3. `git revert [commit ID]`.
4. Type in the new commit message.
5. Save and close
6. Push changes to github
