import subprocess

subprocess.run("python3 udp_echo_server.py & python3 udp_echo_client.py", shell=True)
