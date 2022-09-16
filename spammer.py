from lib2to3.pgen2 import token
from random import randint
import requests
import threading

def spam():
    tokens=open("tokens.txt", "r").read().splitlines()

    while True: 
        r = requests.post("https://staging.fosscord.com/api/v9/channels/1020343865950988490/messages", 
                          headers={
                               "Accept": "*/*",
                              "Accept-Encoding": "gzip, deflate, br",
                              "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                              "Authorization": tokens[randint(0, len(tokens))],
                              "Connection": "keep-alive",
                              "Content-Length": "59",
                              "Content-Type": "application/json",
                              "Cookie": "__stripe_mid=53aaef50-7781-439e-944d-4438e92cbc7d4c65e9; __stripe_sid=ee265b1a-f62d-4d56-a1c9-877cd7210c26cd0343",
                              "Host": "staging.fosscord.com",
                              "Origin": "https://staging.fosscord.com",
                              "Referer": "https://staging.fosscord.com/channels/1020343865904851143/1020343865950988490",
                              "sec-ch-ua": "Microsoft Edge;v=105 Not;A Brand;v=99, Chromium;v=105,",
                              "sec-ch-ua-mobile": "?0",
                              "sec-ch-ua-platform": "Windows",
                              "Sec-Fetch-Dest": "empty",
                              "Sec-Fetch-Mode": "cors",
                              "Sec-Fetch-Site": "same-origin",
                              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42",
                              "X-Debug-Options": "logGatewayEvents,logOverlayEvents,logAnalyticsEvents,bugReporterEnabled",
                              "X-Discord-Locale": "fr",
                              "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDUuMC4xMzQzLjQyIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MTAyMSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                            },
                          json={
                              "content": "sus",
                              "nonce": "1020355999346720768",
                              "tts": "false"
                    })
        print(r.text)

for i in range(1,10) :
    main = threading.Thread(target=spam)
    main.start()