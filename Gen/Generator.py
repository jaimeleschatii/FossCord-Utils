import requests, random, string, time, os
from colorama import Fore,init;init()

class test():
    os.system("cls")
    Randomgen = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(4))
    while True:
        r = requests.post("https://staging.fosscord.com/api/v9/auth/register",
                          headers={
                              "Accept": "*/*",
                              "Accept-Encoding": "gzip, deflate, br",
                              "Accept-Language": "fr-FR,fr;q=0.5",
                              "Connection": "keep-alive",
                              "Content-Length": "94",
                              "Content-Type": "application/json",
                              "Host": "staging.fosscord.com",
                              "Origin": "https://staging.fosscord.com",
                              "Referer": "https://staging.fosscord.com/invite/HWhwaq",
                              "Sec-Fetch-Dest": "empty",
                              "Sec-Fetch-Mode": "cors",
                              "Sec-Fetch-Site": "same-origin",
                              "Sec-GPC": "1",
                              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                              "X-Debug-Options": "logGatewayEvents,logOverlayEvents,logAnalyticsEvents,bugReporterEnabled",
                              "X-Discord-Locale": "fr",
                              "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MTAyMSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                          },
                        json={
                            "username": f"sus_{Randomgen}",
                            "invite": "HWhwaq",
                            "consent": "true",
                            "gift_code_sku_id": "null",
                            "captcha_key": "null"
                        })
        token = r.json()['token']
        print(f"{Fore.LIGHTGREEN_EX}[+] New Tokens "+f"{Fore.LIGHTBLUE_EX}{token}")
        time.sleep(5)
    
        file = open("tokens.txt", "a+")
        file.write(f"{token}"+ '\n')
        file.close()
