| [⬅ 4. Exploring history](04-exploring-history.md) | [Table of Contents](00-contents.md) |  [6. Setting up a remote repository in GitHub ➡](06-remotes-in-github.md) |
| :---- |:----:| ----:|

# 5. Working with branches

![The Git Staging Area](fig/git-staging-area.png)

Often you may want to test out a new feature in some code. You may or may not decide you want to keep this feature and in the mean time you want to make sure you have a version of your script you know works. Branches are instances of a repository that can be edited and version controlled in parallel. You can think of it like making an entire copy of your repository folder that you can edit, without affecting the original versions of your scripts. The advantage of using git to do this (rather that making a repo_copy folder on your computer), is that you can use git tools to manage this code while it's under development and you have the ability to seamlessly merge in your changes into your originals.

Create a file called pluto in your repository, add and commit it
```
$ vi pluto.txt
$ cat pluto.txt
It is so a planet!
git add pluto.txt
git commit -m "Added pluto info"
```

To see what branches are available in your repository, you can type `git branch`. First make sure you're in the planets directory in your home folder:

```
$ cd path-to-planets-dir
$ git branch
* master
```
You see only one branch, "master", which is created when the repository is initialized.

With an argument, the `git branch` command creates a new branch with the given name. Let's make a new experimental branch:

```
$ git branch experimental
  experimental
* master
```

The star indicates we are still currently in the master branch of our repository. To switch branches, we use the `git checkout` command to checkout a different branch. 

```
$ git checkout experimental
Switched to branch 'experimental'
```

Type `git branch` again to see that the star has moved:

```
$ git branch
* experimental
  master
```

Suppose we have some updated information on pluto suggesting it has a heart on its surface, but we aren't sure that we will want to include this detail in our final document. Let's include it in the `pluto.txt` file in our experimental branch:

```
$ vi pluto.txt
$ cat pluto.txt
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
```

We've made this change on our experimental branch. Let's add and commit this change:

```
$ git add pluto.txt
$ git commit -m "Breaking updates about Pluto"
[experimental c5d6cba] Breaking updates about Pluto
 1 file changed, 1 insertion(+)
```

Let's check our status:

```
$ git status
On branch experimental
nothing to commit, working directory clean
```

You can see from the git status output that we are on the experimental branch rather than the master branch. Let's examine the master branch to ensure the original version of our `pluto.txt` doesn't include this sentimental statement:

```
$ git checkout master
Switched to branch 'master'
```

```
$ cat pluto.txt
It is so a planet!
```

As you can see, the master branch does not include our updated notes about Pluto. 

Now we decide we are pretty confident that Pluto's heart is charming, so we want to fold all of the changes we've made on the experimental branch into the master branch. 

To merge two branches together, ensure you are on the branch you want to fold changes *into*. 
In this case, we want to be on the master branch:

```
$ git branch
  experimental
* master
```

Excellent, we are on the right branch. To fold the experimental branch into the master branch, we use the `git merge` command followed by the name of the branch we want to fold *in* to the current branch:

```
$ git merge experimental
Updating ee530d7..c5d6cba
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
```

By default `git merge` also performs a `git commit` if there are no conflicts -- a new line isn't considered a conflict.

Now if we look at our `pluto.txt` file, we see the updates from the experimental branch in the master branch version:

```
$ cat pluto.txt
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
```

We no longer have a use for our experimental branch. To delete a branch you don't need, you can use the `-d` flag of `git branch`:

```
$ git branch -d experimental
Deleted branch experimental (was c5d6cba).
```

Branching and merging can get more complicated with multiple versions. Suppose we want to list all the co-signers of our treatise on Pluto and invite their input, but we don't know yet what everyone will contribute so we aren't sure about the order of names. You can be diplomatic and list the whole team in alphabetical order until the final version. 

```
$ git branch
* master
$ vi pluto.txt
$ cat pluto.txt
Co-signers (alphabetical order for now): Dracula, Frankenstein, Mummy, and Wolfman
It is so a planet!
A planet with a charming heart on its surface; What's not to love?
```

Meanwhile, we get some input from Wolfman that we aren't sure about including, so we create a wolfman branch.

```
$ git branch wolfman
$ git checkout wolfman
M       pluto.txt
Switched to branch 'wolfman'
```

The "M" next to pluto.txt reminds us that there is a modified file in the master branch that was never added and committed. Oops! Let's delete the wolfman branch, fix up the master branch, and start over.

```
$ git checkout master
M       pluto.txt
Switched to branch 'master'
$ git branch -d wolfman
Deleted branch wolfman (was 436c68b).
$ git add pluto.txt
$ git commit -m "added co-signers"
[master 0720f8f] added co-signers
 1 file changed, 1 insertion(+)
$ git branch wolfman
$ git checkout wolfman
Switched to branch 'wolfman'
```

Just to be sure, we can type `git status`.

```
$ git status
On branch wolfman
nothing to commit, working tree clean
```

Now we can add Wolfman's input and move him up the author list.

```
$ vi pluto.txt
$ cat pluto.txt
Co-signers: Wolfman, Dracula, Frankenstein, and Mummy
It is so a planet!
A planet with a heart on its surface; what's not to love?
Pluto & Charon are 2 planets orbiting a center of mass outside either one -- no howling at Charon, it's not a moon
```

Don't forget to add and commit the changes. You can use the shortcut `-a` to do it in one step.

```
$ git commit -a -m "Wolfman says Pluto and Charon are both planets"
[wolfman 5ed0c6f] Wolfman says Pluto and Charon are both planets
 1 file changed, 2 insertions(+), 1 deletion(-)
```

Meanwhile, Dracula sends us his version of `pluto.txt`, so let's return to master and create a dracula branch to hold his version.

```
$ git checkout master
$ git branch dracula
$ git checkout dracula
$ vi pluto.txt
$ cat pluto.txt
Co-signers (alphabetical order for now): Dracula, Frankenstein, Mummy, and Wolfman
It is so a planet!
A planet with a heart on its surface; what's not to love?
And hearts have lots of blood, yum.
$ git commit -a -m "Dracula's version"
```

After some discussion with the other co-signers, everyone agrees that it's worth crusading for both Pluto and Charon to be planets. Let's merge the changes into master.

First, we realize that we don't remember what all Wolfman's changes were. This is a good time for `git diff`.

```
$ git checkout master
$ git diff master wolfman
diff --git a/pluto.txt b/pluto.txt
index 72ab035..c6bbb49 100644
--- a/pluto.txt
+++ b/pluto.txt
@@ -1,3 +1,4 @@
-Co-signers (alphabetical order for now): Dracula, Frankenstein, Mummy, and Wolfman
+Co-signers: Wolfman, Dracula, Frankenstein, and Mummy
 It is so a planet!
 A planet with a heart on its surface; what's not to love?
+Pluto & Charon are 2 planets orbiting a center of mass outside either one -- no howling at Charon, it's not a moon
```

These changes all look good, so let's proceed with the merge.

```
$ git merge wolfman
Updating 0720f8f..5ed0c6f
Fast-forward
 pluto.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
$ git status
On branch master
nothing to commit, working tree clean
```

Notice that git went ahead with all the changes and committed the merge, saying "Fast-forward". This term means that there had been no changes to master since the branch wolfman was created, so git assumed any changes were not conflicts and accepted them all. If you want to avoid accepting changes without getting to look at them, always use `git diff` before `git merge` and make edits manually.

Next we decide to merge dracula into master as well, knowing that the dracula branch split off *before* the latest merge changed the master branch. This time git is alert to potential conflicts.

```
$ git merge dracula
Auto-merging pluto.txt
CONFLICT (content): Merge conflict in pluto.txt
Automatic merge failed; fix conflicts and then commit the result.
```

At this point if we open up `pluto.txt` with vi we'll see that both Wolfman's and Dracula's versions of the last line are shown as choices, whereas Wolfman's new author order is assumed to be correct. Git recognizes that the author order in the dracula branch was from before the wolfman branch was created, so the author order from the wolfman branch takes precedence. However, we have to actually edit the file to remove Dracula's bloodthirsty last line, because git isn't sure whether Wolfman's or Dracula's last lines should be considered better. Again, using `git diff` before git merge would reveal all the differences, allowing us to perform edits manually before merging.

Let's use diff now.

```
$ git diff master dracula
diff --git a/pluto.txt b/pluto.txt
index c6bbb49..bb7d4da 100644
--- a/pluto.txt
+++ b/pluto.txt
@@ -1,4 +1,4 @@
-Co-signers: Wolfman, Dracula, Frankenstein, and Mummy
+Co-signers (alphabetical order for now): Dracula, Frankenstein, Mummy, and Wolfman
 It is so a planet!
 A planet with a heart on its surface; what's not to love?
-Pluto & Charon are 2 planets orbiting a center of mass outside either one -- no howling at Charon, it's not a moon
+And hearts have lots of blood, yum.
```

`git diff` doesn't judge which differences to treat as conflicts, it just shows all of them.  

To complete the merge that failed, we now have to edit the file with the conflicts and commit. Notice that git has modified `pluto.txt` wherever it believed there was a conflict. Wolfman's change — the already merged into master — is preceded by <<<<<<<. Git has then inserted ======= as a separator between the conflicting changes and marked the end of the content from Dracula with >>>>>>>. (The string of letters and digits after that marker identifies the commit.)

It is now up to us to edit this file to remove these markers and reconcile the changes. We can do anything we want: keep the change made in the local repository, keep the change made in the remote repository, write something new to replace both, or get rid of the change entirely. Let's keep Wolfman's author order, but make Dracula feel he was heard by including a less bloodthirsty version of his contribution.

```
$ vi pluto.txt
$ cat pluto.txt
Co-signers: Wolfman, Dracula, Frankenstein, and Mummy
It is so a planet!
A planet with a heart on its surface; what's not to love?
Pluto & Charon are 2 planets orbiting a center of mass outside either one -- no howling at Charon, it's not a moon
And hearts have lots of love.
$ git commit -a -m "compromise version"
[master b7ea33d] compromise version
```

And finally we can clean up. (A nice feature of git is that it will warn you if you try to delete branches with changes that haven't yet been merged into master.)

```
$ git branch -d dracula
Deleted branch dracula (was d409994).
$ git branch -d wolfman
Deleted branch wolfman (was 9ecedff).
```

