# gdriveMounter
### What this does:
This script make rclone run at boot in the background.

### Prerequisites:
A rclone Google Drive remote filesystem with the name "gdrive"

### Install
`wget -qO- https://raw.githubusercontent.com/slashtechno/gdriveMounter/main/gdriveMount.py | python3`

Now you reboot, your rclone remote filesystem (gdrive) will be mounted and the process will be put in the background.


### In case you need a rclone remote filesystem

Run `sudo apt install rclone -y` 

Run `rclone config` 

Press `n` 

Type in `gdrive` and press enter 

Find the the number that corresponds to Google Drive, type that in and press enter 

Leave client_id and client_secret blank, just press enter 


If you want full access to Google Drive, press `1` and enter 

If you want read only access to Google Drive, press `2` and enter 

Just press enter until it asks for advanced config, press `n` 

Press Y for auto config, (if this does not work press n next time) 

Now it should take you to sign in. 

One signed into to Google, go back to your terminal, press `n` for team drive. 

Now press `q`
