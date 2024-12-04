from fabric import Connection

result = Connection('web1.example.com').run('uname -s', hide=True)