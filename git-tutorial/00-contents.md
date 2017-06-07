# Git and GitHub tutorial

## 1. Go [here](https://github.com/capprogram/2017bootcamp-general/blob/master/git-prep.md) if you need a GitHub account or must install Git.

## 2. Configure Git.

On your linux machine, run `git config` (in any directory) to set your name, email, and preferred options.

Examples:

    git config --global user.name “Sheila Kannappan”
    git config --global user.email sheila@physics.unc.edu
    git config --global color.ui "auto"
    git config --global core.autocrlf false
    git config --global core.editor vi

Note `user.name` is not your GitHub username but rather your name.

*(Our git tutorial assumes you will use vi as your editor, but if you wish to use emacs or some other plain text editor as your default, just type `git config --global core.editor "emacs"' or the analogous command.)*

You can check what you’ve done with

    git config --list
    
You can get more details on config option by typing

    git config -h        # short version
    git config --help    # long version

On your laptop, run `git config` with the same answers used above for your linux machine (to get a terminal, under Windows go to start menu and type "gitbash" to search, or under Mac go to spotlight and type "terminal" to search).

## 3. Complete the tutorial below.

### Table of Contents

1. [Automated Version control](01-automated-version-control.md)
2. [Creating a repository](02-creating-a-repository.md)
3. [Tracking changes](03-tracking-changes.md)
4. [Exploring history](04-exploring-history.md)
5. [Working with branches](05-branches.md)
6. [Setting up a remote repository in GitHub](06-remotes-in-github.md)
7. [Collaborating](07-collaborating.md)

### Source

This tutorial borrows heavily from [Software Carpentry's](http://software-carpentry.org/) tutorial [Version control with git](http://swcarpentry.github.io/git-novice/) and Software Carpentry's [branching tutorial from erdavenport](https://github.com/erdavenport/git-lessons), both under a [Creative Commons Attribution license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

## 4. Additional Resources

1. [Git cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
2. [Quick overview](http://rogerdudler.github.io/git-guide/)
