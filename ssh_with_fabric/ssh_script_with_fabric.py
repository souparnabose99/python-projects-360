from fabric import Connection, Config


config = Config(overrides={"sudo": {"password": "xxx112233"}})
conn = Connection("mike@10.10.166.128:22", connect_kwargs={"password": "xxx112233"}, config=config)

