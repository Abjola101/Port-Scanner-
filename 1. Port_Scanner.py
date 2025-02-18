import socket  # Import socket module

# Second function calling
def scan_port(target_ip, port):
    """Attempts to connect to a given port on the target IP."""
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for connection attempt
            result = s.connect_ex((target_ip, port))  # Attempt a connection
            
            if result == 0:
                return True  # The port is open
    
    except Exception as e:
        print(f"Error: {e}")
        
    return False  # The port is closed

# This function is called first.
def scan_ports(target_ip, start_port, end_port):
    """Scans a range of ports on the target IP."""
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port): #if the result from the other function is true, say Port is open
            print(f"Port {port} is open")
    
    print("Scanning complete.")

# Usage
target = input("Enter target IP address: ")
scan_ports(target, 1, 1024)  # Scans well-known ports 1-1024 - modify as needed.

# Example IP from Shodan:
# 213.155.225.186






