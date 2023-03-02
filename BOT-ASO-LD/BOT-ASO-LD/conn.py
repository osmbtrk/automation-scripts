import paramiko

def run_script(host, username, key_path, script_path):
    # Create a new SSH client
    client = paramiko.SSHClient()
    # Set SSH key parameters to automatically add the server's host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to the server
    private_key = paramiko.RSAKey.from_private_key_file(key_path)
    client.connect(host, username=username, pkey=private_key)
    # Run the script using the 'python' command
    stdin, stdout, stderr = client.exec_command('cd ASO-BOT/ && python3 {}'.format(script_path))
    # Print the output of the script
    print(stdout.read().decode())
    print(stderr.read().decode())
    # Close the SSH connection
    client.close()

# Usage example
run_script('', 'osmbt', 'iddd', 'run.py')
