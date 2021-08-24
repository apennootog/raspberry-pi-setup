# Raspberry Pi 4 Setup

This ansible project is for the not so experienced people who want to play with linux and do all kinds of stuff on their raspberry pi but don't want to go trough the hassle of setting the pi up as a linux server.

## Quick Setup

> You will need **SSH** access to your pi, if you don't how to set this up watch [this](https://www.youtube.com/watch?v=63yw7b0NuWc) video.

1. Install git and anible

   ```
   sudo apt install git -y && sudo apt install ansible -y
   ```

2. SSH into your pi and clone this repo

   ```bash
   git clone https://github.com/apennootog/raspberry-pi-setup.git
   ```

3. CD into it

   ```bash
   cd raspberry-pi-setup
   ```

4. Make a copy of the `config.yml.example` and rename it to `config.yml`, you can customize this file to your liking

   > You con do this with nano: `nano config.yml.example` 

5. Install python3 and pip3

   ```
   sudo apt install python3 -y && sudo apt install python3-pip -y
   ```

6. Install the requirements

   ```
   pip3 install -r requirements.txt
   ```

7. Run `hash.py`

   ```bash
   python3 hash.py 
   ```

8. Run the playbook

   ```
   ansible-playbook main.yml -K
   ```

   > If it asks for the become password just type your sudo password in, the default is **raspberry** 

## Features

- Changes to default password to a one you configure
- changes the hostname
- Installs nmap (optional) 
- Updates will come soon