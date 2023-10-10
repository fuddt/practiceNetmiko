from netmiko import ConnectHandler

# Sandboxの接続情報を定義
ios_xr = {
    'device_type': 'cisco_xr',
    'ip': 'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}

# 接続を確立
connection = ConnectHandler(**ios_xr)

# 設定コマンドのリストを定義
config_commands = [
    'interface Loopback0¥n',
    'description Configured by Netmiko'
]

# 設定コマンドを送信
output = connection.send_config_set(config_commands)
print(output)

# 接続を閉じる
connection.disconnect()
