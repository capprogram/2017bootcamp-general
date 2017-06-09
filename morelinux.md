# I. Linux on a department workstation

[This tutorial](http://user.physics.unc.edu/~sheila/tutorials/LinuxTutorial-deptmachine.pdf) is intended to be completed directly on any department linux workstation. The tutorial is specific to the setup here in the UNC Physics & Astronomy Department. It can be done by yourself but works best with a partner.

# II. Remote use of linux on a dept workstation from your laptop

Before attempting to use a dept linux machine remotely from your laptop, you must have an X11 server and an ssh client installed. Here are some free options:

1. Windows users: Follow the directions at [this
    link](https://shareware.unc.edu) to install X-Win32, and also
    install putty from
    [here](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). 
    Note: If you have git installed, you can also use `export DISPLAY=localhost:0.0` to use X-Win32 from your git bash instead of from putty, however the tutorial below is written for putty.

    To make the export command permanent, you can try the following (the changes won't take place till you restart git bash):
    ```
    echo 'export DISPLAY=localhost:0.0' >> ~/.bashrc
    ```

2. Mac users: Install XQuartz from
    [here](http://xquartz.macosforge.org/landing/). An ssh client
    should be installed by default on OS X.

To log in from outside the UNC network, you may also have to use a virtual private network (VPN), which is encrypted. For more on installing VPN, see [this page](http://help.unc.edu/help/frequently-asked-questions-about-vpn/).

Once you have this software installed (and VPN running if needed) then you can complete [this tutorial](http://user.physics.unc.edu/~sheila/tutorials/LinuxTutorial-laptop.pdf). It is nearly identical to the workstation tutorial but with key differences you should note as you go through it.

If you routinely log into a remote server from home, where the connection may be unstable, it is a good idea to learn about “screen”, which enables a terminal to persist “unattached” to a login session after intentional or involuntary logout, so you can reattach to the terminal later. For example, screen can be useful for starting a job you intend to check back on after dinner.

# III. Linux directly on your laptop

Most of you will not have a linux (or a linux virtual machine) installed on your laptops. Nonetheless it's nice to use linux-like interfaces to ensure a uniform experience with vi, git, and ipython across platforms:

* the Mac OS is built on a linux-like base and bringing up the "terminal" application allows you to use most linux commands locally (e.g., you can poke around your Mac file system with cd, pwd, and ls)
* installing git for Windows will provide the "Git Bash" application (search under the start menu), which has all the same functionality as the Mac terminal - visit [this link](https://git-for-windows.github.io) to install git (all defaults are fine except you may prefer to decline credential manager). 

In both of these applications, right-clicking on the window gives access to a copy-paste menu, which should also remind you of the keyboard shortcuts for these commands:

    * Mac: ctrl-shift-c and ctrl-shift-v
    * Win: ctrl-insert and shift-insert
