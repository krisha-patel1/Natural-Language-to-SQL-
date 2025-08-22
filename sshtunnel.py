import paramiko
from getpass import getpass

def run_remote_stub(sql_query):
    ssh_host = "ilab.cs.rutgers.edu"
    ssh_user = input("Enter your NetID: ")
    ssh_pass = getpass("Enter your iLab password: ")

    remote_python_command = f'python3 ~/stub.py "{sql_query}"'

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ssh_host, username=ssh_user, password=ssh_pass)

        stdin, stdout, stderr = client.exec_command(remote_python_command)

        pg_user = ssh_user
        pg_pass = getpass("Enter your PostgreSQL password: ")
        stdin.write(pg_user + "\n")
        stdin.write(pg_pass + "\n")
        stdin.flush()

        output = stdout.read().decode()
        error = stderr.read().decode()

        return output if output else f"Error:\n{error}"

    finally:
        client.close()
