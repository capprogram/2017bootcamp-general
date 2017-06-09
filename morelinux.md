# I. Useful commands     
(play with these and/or discuss with instructor)

alias    
enscript    
wc    
sort    
less    
which    
grep    
grep -H -r "words to find" *    
[locate]    (not available on all machines)    

ctrl-z & fg    
ps aux | grep username    
kill -9 #    
top    

# II. The best thing since sliced bread: 'screen'    

if your processes run under "screen" are slowing down:     
0) Log into whatever machine you want to run the job.     
1) Create a new PAG by running "pagsh -c /bin/tcsh" PAG stands for process authentication group. This way you can start a set of processes that share the same authentication token and they are isolated from your other processes.     
2) start a new screen session     
3) run "reauth" You will be prompted for your password, which will be used to renew your tokens periodically. Remember the PID that reauth tell you, or figure it out later using "ps aux | grep youronyengoeshere"     
4) start python and run job     
5) detach by ctrl-a d and log out (which leaves that pagsh)     
6) later reconnect with a new login (which obviously doesn't know about the old pagsh) and screen -dR     
7) When you are done, kill the PID and exit out of screen and pagsh.     

# III. Linux scripting

Linux can be used as a programming language as well as an operating system -- this is called linux scripting. Most linux scripting capabilities can be accomplished in python, but with reduced efficiency. 

This optional [linux scripting tutorial](https://github.com/capprogram/2017bootcamp-general/blob/master/bashscripting.txt) is best completed after you are comfortable with both linux and the basics of programming in any language. The tutorial goes with this [bashscriptingsolutions](https://github.com/capprogram/2017bootcamp-general/blob/master/bashscriptingsolutions/) directory and this [bashscriptingfinalpuzzle](https://github.com/capprogram/2017bootcamp-general/blob/master/bashscriptingfinalpuzzle/) directory.
