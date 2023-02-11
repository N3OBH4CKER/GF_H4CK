import sys, time, os, random

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def rm(n):
    up = '\x1b[1A'
    erase = '\x1b[2K'
    print n
    time.sleep(0.1)                                                        
    sys.stdout.write(up)
    sys.stdout.write(erase)

                                                                       
def logo1():
    logo2 = ' -----------------------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n(  __)\\  ____--------------_------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__(~)    \xe2\x80\xa2||\xe2\x80\xa2ar noi single thaka----\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__\\~~) \xe2\x80\xa2||\xe2\x80\xa2DHAKAR KOCHI MAL --------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__(-----\\  \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2------IS HERE BRO-------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa6-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa7-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa5-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n\x1b[1;91m=======================================\n\x1b[1;96mAuthor  \x1b[1;93m: \x1b[1;92mN3OB H4CKER \n\x1b[1;96mDeveloper \x1b[1;93m: \x1b[1;  N3OB X WASIF\n\x1b[1;96mFacebook  \x1b[1;93m: \x1b[1;  www.facebook.com/100074591152479\n\n\x1b[1;96mHack \x1b[1;93m: \x1b[1;92mGF DHAKA\n\x1b[1;91m======================================='
    print logo2
    
    


def logo():
    os.system('figlet -f big GF_H4CKER')
    bannerr = '\x1b[1;91m=======================================\n\x1b[1;96mAuthor  \x1b[1;93m: \x1b[1;92mN3OB-H4CKER\n\x1b[1;96mDeveloper \x1b[1;93m: \x1b[1;  N3OB X WASIF\n\x1b[1;96mFacebook  \x1b[1;93m: \x1b[1;  www.facebook.com/100074591152479\n\x1b[1;96mHack \x1b[1;93m: \x1b[1;93m: \x1b[1;92mGF DHAKA\n\x1b[1;91m======================================='
    print bannerr

def logger():
    os.system('clear')
    logo()
    CorrectUsername = 'N3OB'
    CorrectPassword = 'DHAKA'
    loop = 'true'
    while loop == 'true':
        username = raw_input('\n\x1b[1;95mUSERNAME:\x1b[1;93m ')
        if username == CorrectUsername:
            password = raw_input('\n\x1b[1;95mPASSWORD:\x1b[1;93m ')
            if password == CorrectPassword:
                print '\nAPPROVED!'
                os.system('xdg-open https://www.facebook.com/100074591152479')
                time.sleep(1)
                loop = 'false'
            else:
                print 'wrong password'
                os.system('xdg-open https://www.facebook.com/100074591152479')
                os.system('clear')
                logo()
        else:
            print 'wrong username'
            os.system('xdg-open https://facebook.com/groups/1781194432004610/')
            os.system('clear')
            logo()

    os.system('clear')
    
def main():
    logger()
    logo1()
    print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mSearch your GF \x1b[1;96m[\xe2\x98\x86]\n'
    idd = raw_input('\x1b[1;96m[+] \x1b[1;93mYour gf name \x1b[1;91m: \x1b[1;92m')
    gof = '\n\x1b[1;91m   \xf0\x9f\x94\xb0\x1b[1;95m---------------\x1b[1;92mFinding ' + idd + ' \x1b[1;95m---------------\x1b[1;91m\xf0\x9f\x94\xb0\n'
    psb(gof)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Please Wait........')
    for persent in range(101):
        per = str(persent)
        hulu = '\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Finding Gf....\x1b[1;96m' + per + '%'
        rm(hulu)

    print hulu
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Grabbing your Gf.......')
    time.sleep(2)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Fetching Info.......')
    gf = ('https://www.facebook.com/profile.php?id=100077474200626','https://www.facebook.com/alvera.afiya','https://www.facebook.com/profile.php?id=100086773283531','https://www.facebook.com/profile.php?id=100049686137431','https://www.facebook.com/profile.php?id=100085474182552','https://www.facebook.com/profile.php?id=100070602109376','https://www.facebook.com/profile.php?id=100089706226589','https://www.facebook.com/profile.php?id=100089603351934','https://www.facebook.com/profile.php?id=100083940174121','https://www.facebook.com/profile.php?id=100079156186900','https://www.facebook.com/nahidasrabonti.borsha','https://www.facebook.com/profile.php?id=100088505822764','https://www.facebook.com/profile.php?id=100086148312815','https://www.facebook.com/profile.php?id=100083670402490','https://www.facebook.com/profile.php?id=100090172086100','https://www.facebook.com/profile.php?id=100090102757846','https://www.facebook.com/profile.php?id=100089715846402','https://www.facebook.com/profile.php?id=100089904293992','https://www.facebook.com/profile.php?id=100090052786063','https://www.facebook.com/profile.php?id=100089880024525','https://www.facebook.com/profile.php?id=100078046058366','https://www.facebook.com/profile.php?id=100081612426726','https://www.facebook.com/profile.php?id=100087382990630','https://www.facebook.com/profile.php?id=100080478870506','https://www.facebook.com/profile.php?id=100089547218172','https://www.facebook.com/profile.php?id=100089358597221','https://www.facebook.com/profile.php?id=100085944587598','https://www.facebook.com/profile.php?id=100085944587598','https://www.facebook.com/profile.php?id=100088664244826','https://www.facebook.com/profile.php?id=100090455550865','https://www.facebook.com/profile.php?id=100090102757846','https://www.facebook.com/profile.php?id=100082246477072','https://www.facebook.com/profile.php?id=100081776890621','https://www.facebook.com/profile.php?id=100089282422146','https://www.facebook.com/profile.php?id=100088829527286','https://www.facebook.com/profile.php?id=100085688337684','https://www.facebook.com/profile.php?id=100086447997094','https://www.facebook.com/profile.php?id=100087382990630','https://www.facebook.com/profile.php?id=100090136753439','https://www.facebook.com/profile.php?id=100089594168729','https://www.facebook.com/profile.php?id=100090135370306','https://www.facebook.com/profile.php?id=100090081014149','https://www.facebook.com/profile.php?id=100075151705897','https://www.facebook.com/profile.php?id=100075248725892','https://www.facebook.com/profile.php?id=100090167077804','https://www.facebook.com/profile.php?id=100090504930224','https://www.facebook.com/profile.php?id=100088482084172','https://www.facebook.com/profile.php?id=100090419372152','https://www.facebook.com/profile.php?id=100027996700932','https://www.facebook.com/profile.php?id=100090335522807','https://www.facebook.com/profile.php?id=100090275887986','https://www.facebook.com/profile.php?id=100087937353053','https://www.facebook.com/mdmamun.howlader.31924','https://www.facebook.com/profile.php?id=100074035453160','https://www.facebook.com/profile.php?id=100089698939282','https://www.facebook.com/profile.php?id=100086722696544','https://www.facebook.com/profile.php?id=100081557216497','https://www.facebook.com/profile.php?id=100089972566661','https://www.facebook.com/profile.php?id=100090186818844','https://www.facebook.com/profile.php?id=100090359675774','https://www.facebook.com/profile.php?id=100088891848851','https://www.facebook.com/profile.php?id=100090021828788','https://www.facebook.com/profile.php?id=100089954720085','https://www.facebook.com/profile.php?id=100074035453160','https://www.facebook.com/profile.php?id=100090379533805')      
    v = random.choice(gf)
    bof = '\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m We Cant Found ' + idd + '\n\tBut we Found Kochi Mal ' + v
    psb(bof)
    p = 'xdg-open ' + v
    os.system(p)
    time.sleep(2)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;91m  !!!!!!!!!!!!!.....please wait.......!!!!!!!!!!!')
    time.sleep(5)
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m This girl has been found as your girlfriend...')
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Send a friend request this kochi Mal and enjoy......')
    psb('\x1b[1;91m[\x1b[1;37;40m+\x1b[1;91m]\x1b[1;92m Do not take it seriously bcz its just make for fun.......')


main()