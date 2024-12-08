from fabric import Connection, Config


config = Config(overrides={"sudo": {"password": "xxx112233"}})
conn = Connection(
    "bose@192.168.0.0:20",
    connect_kwargs={"password": "xxx112233"},
    config=config
)

conn.run("ping -c 2 www.google.com")
conn.sudo("systemctl restart nfs-kernel-server")

# transferring files
conn.get("remote_file_path", "local_file_path")
conn.put("local_file_path", "remote_file_path")

