from mcstatus import MinecraftServer
from random import random
import math
import re


# check server
def check(ip):
    try:
        server = MinecraftServer.lookup(ip)
        data = server.status()

        if data is False:
            print(f'[-] {ip}')
            return
        else:
            server = {
                'ip_address': ip,
                'version': data.version.name,
                'motd': clear_motd(data.description),
                'player_count': data.players.online,
                'player_max': data.players.max,
                'players': []
            }
            if data.players.sample is not None:
                for player in data.players.sample:
                    server['players'].append(dcolor(player.name))
            write(server)
            print(f'[+] > {ip}')

    except:
        return False


# Random number function
def random_number(minimum, maximum):
    return math.floor(random() * (maximum - minimum + 1) + minimum)


def clear_motd(motd):
    result = ""
    if "extra" in motd:
        motd = motd["extra"]
        for part in motd:
            result = result + part["text"]
    else:
        result = motd["text"]
    return dcolor(result)


def dcolor(text):
    return re.sub(r'[§]\w', r'', text)


def write(server):
    file = open("output.txt", "a")
    sep = ',\n'
    to_write = \
        f'Server ip: {server["ip_address"]}\n' \
        f'Server version: {server["version"]}\n' \
        f'Server players: {server["player_count"]}/{server["player_max"]}\n' \
        f'Server MOTD:\n{server["motd"]}\n' \
        f'Players list:\n{sep.join(server["players"])}' \
        f'- - - - - - - - - -   S e p a r a t o r   - - - - - - - - - -'
    file.write(to_write)


def main():
    ip = f"{random_number(0, 255)}.{random_number(0, 255)}.{random_number(0, 255)}.{random_number(0, 254)}"
    check(ip)
    main()


if __name__ == "__main__":
    main()
