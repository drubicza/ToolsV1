import os, sys, time, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
p = '\x1b[1;97m'
b = '\x1b[1;94m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
bm = '\x1b[1;96m'

def clear():
    os.system('clear')


os.system('clear')
time.sleep(1)

def menu():
    print h + '-------------------------------------------------------------'
    print k + '[+]\x1b[1;91m Author    \x1b[1;92m: \x1b[1;96mMr.Crabs               \x1b[1;93m                    [+] '
    print k + '[+] \x1b[1;91mGithub    \x1b[1;92m:\x1b[1;94m github.com/crabsgans           \x1b[1;93m            [+] '
    print k + '[+] \x1b[1;97mThanks To\x1b[1;92m :\x1b[1;97m |Kupang Burik|Pickacuh Burik|Mr.Berdasi   \x1b[1;93m [+]'
    print k + '[+] \x1b[1;97mTeam   \x1b[1;92m   :\x1b[1;91m |SFO|BCT|HCT                               \x1b[1;93m[+]'
    print h + '-------------------------------------------------------------'
    print b + '==============================='
    print k + '[1].Hack Facebook'
    print b + '==============================='
    print h + '[2].SpamCalls'
    print b + '==============================='
    print p + '[3].Lacak Lokasi'
    print b + '==============================='
    print u + '[4].Scanner Web Vuln'
    print b + '==============================='
    print p + '[5].sms gratis'
    print b + '==============================='
    print m + '[6].Ddos Attack'
    print b + '==============================='
    print bm + '[7].Spam Sms'
    print b + '==============================='
    print h + '[8].Hack CCTV'
    print b + '==============================='
    print k + '[9].Hack Camera'
    print b + '==============================='
    print u + '[10].Phising Akun Sosmed'
    print b + '==============================='
    print m + '[0].Exit'
    print b + '==============================='
    print m + 'Note : Script Ini akan di update Ke Versi Selanjutnya'
    pilih = raw_input(h + 'Pilih Nomernya : \x1b[1;93m')
    if pilih == '1':
        os.system('clear')
        os.system('git clone https://github.com/Crabsgans/Fb\n\t\t                   cd Fb\n\t\t                   python2 dark.py')
    if pilih == '2':
        os.system('clear')
        os.system('git clone https://github.com/Crabsgans/Call\n                           cd Call\n                           php spam.php')
    if pilih == '3':
        os.system('clear')
        os.system('git clone https://github.com/thelinuxchoice/locator\n      \t                 cd locator\n      \t                 bash locator.sh')
    if pilih == '4':
        os.system('clear')
        os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK\n                          cd RED_HAWK\n                          chmod +x rhawk.php\n                          php rhawk.php')
    if pilih == '5':
        os.system('clear')
        os.system('git clone https://github.com/Crabsgans/sms-\n                          cd sms-\n                          python sms.py')
    if pilih == '6':
        os.system('clear')
        os.system('git clone https://github.com/cyweb/hammer\n      cd hammer\n      python hammer.py')
    if pilih == '7':
        os.system('clear')
        os.system('git clone https://github.com/TERMUXID3/brutal-sms\ncd brutal-sms\npython2 run.py')
    if pilih == '8':
        os.system('clear')
        os.system('git clone https://github.com/kancotdiq/ipcs\n      cd ipcs\n      python2 scan.py')
    if pilih == '9':
        os.system('clear')
        os.system('git clone https://github.com/thelinuxchoice/saycheese\n      cd saycheese\n      bash saycheese.sh')
    if pilih == '10':
        os.system('clear')
        os.system('git clone https://github.com/thelinuxchoice/shellphish\n       cd shellphish\n       bash shellphish.sh')
    if pilih == '0':
        print '[!] KELUAR '
        time.sleep(1)
        os.system('exit')
    else:
        print 'pilih yang benar'
        time.sleep(2)
        os.system('clear')
        menu()


print h + '[+] \x1b[1;93mmasukan password\x1b[1;92m [+] '
print h + '=========================='
pas = raw_input(':\x1b[1;96m')
if pas == 'crabsgans':
    time.sleep(3)
    print 'password diterima'
    time.sleep(1)
    os.system('clear')
    menu()
else:
    time.sleep(3)
    print 'password salah'
    os.system('exit')
