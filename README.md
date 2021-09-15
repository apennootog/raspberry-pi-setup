<p align="center">
   <img src="Images/rpi.png" width="100" height="130">
</p>

# Raspberry Pi 4 Setup

This ansible project will set up your raspberry pi, it will install some packages and change the default password. It is a quick and easy way to do all the setup work.

## Quick Setup

> You will need **SSH** access to your pi, if you don't how to set this up watch [this](https://www.youtube.com/watch?v=63yw7b0NuWc) video.

1. Update cache and install pip3 and git

   ```bash
   sudo apt update && sudo apt install git python3-pip -y
   ```

2. Install ansible

   ```bash
   pip3 install ansible
   ```

   > **You need to install ansible with pip** because with apt you don't get the latest version

3. Clone this repo and cd into it 

   ```bash
   git clone https://github.com/apennootog/raspberry-pi-setup.git && cd raspberry-pi-setup
   ```

4. Install ansible requirements

   ```bash
   ansible-galaxy collection install -r requirements.yml
   ```

   > If ansible-galaxy is not recognized as a command reboot your pi by doing `sudo reboot`

5. Copy `config.yml.example` to `config.yml` and customize it to your liking

   > You can do this with any command line based text editor, for example: nano (`nano config.yml.example`)

6. Run the playbook

   ```bash
   ansible-playbook main.yml -k -K
   ```

   > The default ssh password is **raspberry** and the sudo password should be the same if you haven't changed it

   

## Features

- Changes to default password to a one you configure
- Updates the pi
- Installs nmap (optional)
- Installs nodejs (optional)
- Installs docker (optional)
- Installs python3 and pip3 
- Updates will come soon



## License

MIT



## Author

This project was created in 2021 by [apennootog](https://github.com/apennootog)  