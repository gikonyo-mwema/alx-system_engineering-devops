# Lost Access to Web servers and Load Balances.

![Alt Text](https://media0.giphy.com/media/WqDRe5JBggRva/200.gif?cid=790b7611fwz5f56x5lzmvzwiw00o111v972k08u6z1xl92a3&ep=v1_gifs_search&rid=200.gif&ct=g)

## Issue Summary
On May 4th, I Lost access to  my web servers and load balancer. All services that required use of web servers were halted including working, deploying and validating ALX course tasks. The root cause of corruption of my linux Virtual machine.

## Timeline 
* 3:30 AM: Starts windows machine
* 3:40 AM: Linux virtual machine fails to load
* 3:45 AM: Full restart
* 3:50 AM: Virtual machine issue persist
* 4:00 AM: Runs Antivirus on window machine
* 4:10 AM: Windows update start
* 4:30 AM: Update and restart
* 4:50 AM: Creates an new machine using previously save image of linux
* 5:00 AM: Configuration and load fails
* 6:00 AM: Download new image (linux 22)
* 6:30 AM: Virtual box setup and running
* 6:45 AM: Essential programs installed - git, vi, mysql …
* 6:50 AM: Git clone of files from github
* 7:00 AM: Connection to web servers fail 
* 9:00 AM: Issues persist
* 9:10 AM: Request new web servers from ALX
* 9:30 AM: New web servers assigned configuration begins
* 12:00 PM: Successful configuration of both web servers and load balancer
* 1:00 PM: New fully functional system running!
* 2:00 PM: Backup of important files 
* 3:00 PM: Back to course work and tasks

## Root cause and resolution 
The root cause of the issues was corruption of the linux virtual machine files by a virus in my windows host computer. This led to the vm using up all the memory and cpu leading to a freeze. The linux would keep trying to load for a long time without results. 
The solution was to run antivirus software and update windows. Then the vm causing the issues was discarded. A new version V22 was installed and set up.
## Corrective and preventative 
A backup copy of the public and private keys used to connect to the web servers has been created. Also configuration files have been backed up for faster future recovery.
