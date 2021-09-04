# Raspberry Pi 4 Setup

This ansible project will set up your raspberry pi, it will install some packages and change the default password. It is a quick and easy way to do all the setup work.

## Quick Setup

> You will need **SSH** access to your pi, if you don't how to set this up watch [this](https://www.youtube.com/watch?v=63yw7b0NuWc) video.

1. Update cashe and install ansible and git

   ```bash
   sudo apt update && sudo apt install git ansible -y
   ```

2. Clone this repo and cd into it 

   ```bash
   git clone https://github.com/apennootog/raspberry-pi-setup.git && cd raspberry-pi-setup
   ```

3. Copy `config.yml.example` to `config.yml` and customize it to your liking

   > You can do this with any command line based text editor, for example: nano (`nano config.yml.example`)

4. Run the playbook

   ```bash
   ansible-playbook main.yml -k -K
   ```

   > The default ssh password is **rasberry** and the sudo password should be the same if you haven't changed it

   

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