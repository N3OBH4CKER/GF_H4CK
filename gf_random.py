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
    logo2 = ' -----------------------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n(  __)\\  ____--------------_------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__(~)    \xe2\x80\xa2||\xe2\x80\xa2 KI VAI SINGLE NAKI----\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__\\~~) \xe2\x80\xa2||\xe2\x80\xa2BD KOCHI MAL --------------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__(-----\\  \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2------IS HERE BRO-------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa6-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa7-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n|__~~~\\ \xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-----\xe2\x96\x88-------\xe2\x91\xa5-------\xe2\x96\x88------\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2\n\x1b[1;91m=======================================\n\x1b[1;96mAuthor  \x1b[1;93m: \x1b[1;92mN3OB H4CKER \n\x1b[1;96mDeveloper \x1b[1;93m: \x1b[1;  N3OB X WASIF\n\x1b[1;96mFacebook  \x1b[1;93m: \x1b[1;  www.facebook.com/100074591152479\n\n\x1b[1;96mHack \x1b[1;93m: \x1b[1;92mGF_RANDOM\n\x1b[1;91m======================================='
    print logo2
    
    


def logo():
    os.system('figlet -f big GF_H4CKER')
    bannerr = '\x1b[1;91m=======================================\n\x1b[1;96mAuthor  \x1b[1;93m: \x1b[1;92mN3OB-H4CKER\n\x1b[1;96mDeveloper \x1b[1;93m: \x1b[1;  N3OB X WASIF\n\x1b[1;96mFacebook  \x1b[1;93m: \x1b[1;  www.facebook.com/100074591152479\n\x1b[1;96mHack \x1b[1;93m: \x1b[1;93m: \x1b[1;92mGF_RANDOM\n\x1b[1;91m======================================='
    print bannerr

def logger():
    os.system('clear')
    logo()
    CorrectUsername = 'N3OB'
    CorrectPassword = 'H4CKER'
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
    gf = ('https://www.facebook.com/profile.php?id=100077474200626','https://www.facebook.com/alvera.afiya','https://www.facebook.com/profile.php?id=100086773283531','https://www.facebook.com/profile.php?id=100049686137431','https://www.facebook.com/profile.php?id=100085474182552','https://www.facebook.com/profile.php?id=100070602109376','https://www.facebook.com/profile.php?id=100089706226589','https://www.facebook.com/profile.php?id=100089603351934','https://www.facebook.com/profile.php?id=100083940174121','https://www.facebook.com/profile.php?id=100079156186900','https://www.facebook.com/nahidasrabonti.borsha','https://www.facebook.com/profile.php?id=100088505822764','https://www.facebook.com/profile.php?id=100086148312815','https://www.facebook.com/profile.php?id=100083670402490','https://www.facebook.com/profile.php?id=100090172086100','https://www.facebook.com/profile.php?id=100090102757846','https://www.facebook.com/profile.php?id=100089715846402','https://www.facebook.com/profile.php?id=100089904293992','https://www.facebook.com/profile.php?id=100090052786063','https://www.facebook.com/profile.php?id=100089880024525','https://www.facebook.com/profile.php?id=100078046058366','https://www.facebook.com/profile.php?id=100081612426726','https://www.facebook.com/profile.php?id=100087382990630','https://www.facebook.com/profile.php?id=100080478870506','https://www.facebook.com/profile.php?id=100089547218172','https://www.facebook.com/profile.php?id=100089358597221','https://www.facebook.com/profile.php?id=100085944587598','https://www.facebook.com/profile.php?id=100085944587598','https://www.facebook.com/profile.php?id=100088664244826','https://www.facebook.com/profile.php?id=100090455550865','https://www.facebook.com/profile.php?id=100090102757846','https://www.facebook.com/profile.php?id=100082246477072','https://www.facebook.com/profile.php?id=100081776890621','https://www.facebook.com/profile.php?id=100089282422146','https://www.facebook.com/profile.php?id=100088829527286','https://www.facebook.com/profile.php?id=100085688337684','https://www.facebook.com/profile.php?id=100086447997094','https://www.facebook.com/profile.php?id=100087382990630','https://www.facebook.com/profile.php?id=100090136753439','https://www.facebook.com/profile.php?id=100089594168729','https://www.facebook.com/profile.php?id=100090135370306','https://www.facebook.com/profile.php?id=100090081014149','https://www.facebook.com/profile.php?id=100075151705897','https://www.facebook.com/profile.php?id=100075248725892','https://www.facebook.com/profile.php?id=100090167077804','https://www.facebook.com/profile.php?id=100090504930224','https://www.facebook.com/profile.php?id=100088482084172','https://www.facebook.com/profile.php?id=100090419372152','https://www.facebook.com/profile.php?id=100027996700932','https://www.facebook.com/profile.php?id=100090335522807','https://www.facebook.com/profile.php?id=100090275887986','https://www.facebook.com/profile.php?id=100087937353053','https://www.facebook.com/mdmamun.howlader.31924','https://www.facebook.com/profile.php?id=100074035453160','https://www.facebook.com/profile.php?id=100089698939282','https://www.facebook.com/profile.php?id=100086722696544','https://www.facebook.com/profile.php?id=100081557216497','https://www.facebook.com/profile.php?id=100089972566661','https://www.facebook.com/profile.php?id=100090186818844','https://www.facebook.com/profile.php?id=100090359675774','https://www.facebook.com/profile.php?id=100088891848851','https://www.facebook.com/profile.php?id=100090021828788','https://www.facebook.com/profile.php?id=100089954720085','https://www.facebook.com/profile.php?id=100074035453160','https://www.facebook.com/profile.php?id=100090379533805','https://www.facebook.com/mitu.lslam.100','https://www.facebook.com/profile.php?id=100090116743390','https://www.facebook.com/profile.php?id=100074765561154','https://www.facebook.com/profile.php?id=100082370846542','https://www.facebook.com/profile.php?id=100083579511620','https://www.facebook.com/profile.php?id=100086462804489','https://www.facebook.com/profile.php?id=100090435210489','https://www.facebook.com/profile.php?id=100088482084172','https://www.facebook.com/mimjahan.mimjahan.5680','https://www.facebook.com/labonna.islam.16','https://www.facebook.com/mahi.afrin.7509','https://www.facebook.com/profile.php?id=100088298364095','https://www.facebook.com/fariakhan.onima','https://www.facebook.com/jhorasorker.jhorasorker','https://www.facebook.com/profile.php?id=100089970528416','https://www.facebook.com/profile.php?id=100008515177870','https://www.facebook.com/profile.php?id=100090110231896','https://www.facebook.com/profile.php?id=100089392901103','https://www.facebook.com/profile.php?id=100079283826189','https://www.facebook.com/profile.php?id=100087855519011','https://www.facebook.com/profile.php?id=100075902888029','https://www.facebook.com/profile.php?id=100082195016546','https://www.facebook.com/profile.php?id=100027779871604','https://www.facebook.com/profile.php?id=100079230700592','https://www.facebook.com/profile.php?id=100089960718299','https://www.facebook.com/ariyana.ayat.222','https://www.facebook.com/profile.php?id=100090234573720','https://www.facebook.com/profile.php?id=100010082111591','https://www.facebook.com/profile.php?id=100090209139781','https://www.facebook.com/profile.php?id=100089363824398','https://www.facebook.com/profile.php?id=100090147403404','https://www.facebook.com/profile.php?id=100090151032496','https://www.facebook.com/anikazannat.annu','https://www.facebook.com/profile.php?id=100082128913707','https://www.facebook.com/profile.php?id=100081837232976','https://www.facebook.com/profile.php?id=100085228020534','https://www.facebook.com/profile.php?id=100088911527268','https://www.facebook.com/profile.php?id=100078717460824','https://www.facebook.com/profile.php?id=100088555606499','https://www.facebook.com/profile.php?id=100089854147134','https://www.facebook.com/profile.php?id=100089925654257','https://www.facebook.com/profile.php?id=100090125830893','https://www.facebook.com/profile.php?id=100090440161469','https://www.facebook.com/profile.php?id=100089774847418','https://www.facebook.com/profile.php?id=100090223390464','https://www.facebook.com/profile.php?id=100089830676731','https://www.facebook.com/profile.php?id=100089245385372','https://www.facebook.com/profile.php?id=100089921272835','https://www.facebook.com/profile.php?id=100089706867666','https://www.facebook.com/profile.php?id=100089851372475','https://www.facebook.com/profile.php?id=100090291936348','https://www.facebook.com/profile.php?id=100090435210489','https://www.facebook.com/profile.php?id=100090359675774','https://www.facebook.com/profile.php?id=100083369514797','https://www.facebook.com/profile.php?id=100046525066021','https://www.facebook.com/profile.php?id=100087280873892','https://www.facebook.com/profile.php?id=100074544096002','https://www.facebook.com/rimjhim.sharkar.56','https://www.facebook.com/alpita.khan.902','https://www.facebook.com/profile.php?id=100079163566061','https://www.facebook.com/profile.php?id=100088995497453','https://www.facebook.com/profile.php?id=100090448502007','https://www.facebook.com/profile.php?id=100088732436731','https://www.facebook.com/profile.php?id=100082378486060','https://www.facebook.com/profile.php?id=100089858637595','https://www.facebook.com/profile.php?id=100090128714847','https://www.facebook.com/profile.php?id=100081763102715','https://www.facebook.com/profile.php?id=100090355748134','https://www.facebook.com/profile.php?id=100085676940831','https://www.facebook.com/profile.php?id=100089761239933','https://www.facebook.com/profile.php?id=100090257290241','https://www.facebook.com/profile.php?id=100086056973989','https://www.facebook.com/profile.php?id=100090168248794','https://www.facebook.com/profile.php?id=100089903114823','https://www.facebook.com/profile.php?id=100089928324445','https://www.facebook.com/profile.php?id=100090278320265','https://www.facebook.com/profile.php?id=100089951540585','https://www.facebook.com/profile.php?id=100090005163029','https://www.facebook.com/profile.php?id=100090441091318','https://www.facebook.com/profile.php?id=100087198145375','https://www.facebook.com/profile.php?id=100088348854693','https://www.facebook.com/profile.php?id=100090131532483','https://www.facebook.com/profile.php?id=100090460712918','https://www.facebook.com/profile.php?id=100090220177827','https://www.facebook.com/profile.php?id=100090217121470','https://www.facebook.com/profile.php?id=100085299993354','https://www.facebook.com/evana.eva.9212','https://www.facebook.com/profile.php?id=100089821975872','https://www.facebook.com/profile.php?id=100089466014756','https://www.facebook.com/profile.php?id=100090178633224','https://www.facebook.com/profile.php?id=100082238575595','https://www.facebook.com/profile.php?id=100090074745152','https://www.facebook.com/profile.php?id=100090239581595','https://www.facebook.com/mahinur.mahi.927','https://www.facebook.com/profile.php?id=100090116055622','https://www.facebook.com/profile.php?id=100090360784545')      
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