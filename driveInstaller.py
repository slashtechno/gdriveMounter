import os


os.system("pip3 install keyboard") #install keyboard module

os.system("cd ~")
bashrc=open(".bashrc","a") #open .bashrc in append mode
bashrc.write("python3 ~/gdriveMounter/background.py")
bashrc.close
os.system("mkdir ~/gdriveMounter && cd ~/gdriveMounter") # Create program's directory and cd into it
#Add wget command here for script 