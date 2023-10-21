import socket
import time

servers = [
        ["WalkerCraft", 25565],
        ["Modded WalkerCraft", 25566],
        # ["All the Walkers 9", 25509],
]

BROADCAST_IP = "255.255.255.255"
BROADCAST_PORT = 4445

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("Broadcasting Minecraft servers to LAN")

while 1:
        for server in servers:
                msg = f"[MOTD]{server[0]}[/MOTD][AD]{server[1]}[/AD]"
                sock.sendto(msg.encode(), (BROADCAST_IP, BROADCAST_PORT))
        time.sleep(1.5)
