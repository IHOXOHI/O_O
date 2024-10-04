# OO
A secure boot, very simple, to all Micropython boards.
The oo.py use the 'VCP+MCP' mode, so the file system could be mounted by a computer... In this case, the security depend too of the computer...
The ooo.py use only the VCP mode, so the coast is no file system... As far I know, only screen or mpremote softwares works to have acces to the board (they don't reboot the board)... So, you can use too 'shells_commands.py' which contain basics commands to copy and view a file.
On the pyboard, the 'safe mode' break this security... If someone has an advice on how disable this function... Thanks. 
