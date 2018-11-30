import paramiko

client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    '192.168.205.11',
    username='diurno',
    password='diurno',
    port='22'
)

stdin, stdout, stderr = client.exec_command('ls -la')

if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))