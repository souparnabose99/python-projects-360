from fabric import Connection, Config


config = Config(overrides={"sudo": {"password": "xxx112233"}})
conn = Connection(
    "bose@192.168.0.0:20",
    connect_kwargs={"password": "xxx112233"},
    config=config
)

