import requests

url = 'https://api.tracker.yandex.net/v2/issues'

headers = {
    'Authorization': 'OAuth y0_AgAAAAANtcFqAAr2aAAAAAD0PvXsTnXbRKw-RzeSGuyMVve_CcFVaZY',
    'X-Cloud-Org-ID': 'bpfvb38s0s3vl8njr3n6',
    'Content-Type': 'application/json'
}

data = {
    'queue': 'TEAMCITYBUILDFA',
    'summary': 'Fix failed build',
    'assignee': 'captainrall'
}

response = requests.post(url, headers=headers, json=data)
print(response)
