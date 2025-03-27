import paramiko
import time

# Device details for Router0
ip = "192.168.10.1"
username = "admin"
password = "admin123"

try:
    print(f"Connecting to Router0 ({ip})...")
    # Create SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to Router0
    ssh.connect(ip, username=username, password=password, timeout=10)

    # Start an interactive shell
    shell = ssh.invoke_shell()
    time.sleep(1)

    # Send command
    shell.send("show version\n")
    time.sleep(2)

    # Read output
    output = shell.recv(65535).decode('utf-8')
    print(f"Output from Router0:\n{output}")

    # Close connection
    ssh.close()
    print("Disconnected from Router0.")

except Exception as e:
    print(f"Failed to connect to Router0: {str(e)}")