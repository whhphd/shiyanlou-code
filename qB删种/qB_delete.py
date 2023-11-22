import time

import qbittorrentapi

# 请替换以下变量为您的qBittorrent Web API凭据
qbt_host = ''
qbt_username = ''
qbt_password = ''

# 连接到qBittorrent Web API
client = qbittorrentapi.Client(host=qbt_host, username=qbt_username, password=qbt_password)
try:
    client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(f"Error: {e}")
    exit()

# 获取所有任务
torrents = client.torrents_info()

# 合并具有相同名称的任务，并取其中最后活动时间的最大值
torrents_dict = {}
for torrent in torrents:
    if torrent.name not in torrents_dict:
        torrents_dict[torrent.name] = torrent
    else:
        if torrent.last_activity > torrents_dict[torrent.name].last_activity:
            torrents_dict[torrent.name] = torrent

# 筛选最后活动时间大于30天的任务
# 注意：我们将25天转换为秒（1天 = 86400秒）
filtered_torrents = [torrent for torrent in torrents_dict.values() if time.time() - torrent.last_activity > 30 * 86400]

# 输出torrent.name
for torrent in filtered_torrents:
    print(torrent.name)