from passlib.hash import sha512_crypt;
import getpass;
import yaml;

config = open("./config.yml")
config_parsed = yaml.load(config, Loader=yaml.FullLoader)

hash = sha512_crypt.using(rounds=5000).hash(config_parsed.get("pi_user_password"))

data = {
    "hash": hash
}

hashed = open("./Files/hashed.yml", "w")
yaml.dump(data, hashed)

config.close()
hashed.close()



