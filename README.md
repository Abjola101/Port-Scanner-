# Port-Scanner-
This program is a python port scanner to determine open ports on particular IP addresses. It takes port 1 to 1024 and iteratively checks each port within that range by making connections to each one on the target IP to identify open ports, the ports are outputted when found when the program is running.

The program is made up of two Python functions. scan_ports and scan_port.

scan_ports:
- Takes each port one at a time and parses it to scan_port function. 
- Iterates the port number each iteration.

scan_port:
- Attempts to make a connection to that specific iteration port on the host. 
- If no connection can be made, port is closed is outputted.

Usage:
- Simply provide an IP address when running the program in the user input and press enter. 
- The program will then run and output open ports in real time. 
