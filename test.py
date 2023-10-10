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

# コマンドを実行
output = connection.send_command('show interfaces')
print(output)

# 接続を閉じる
connection.disconnect()
