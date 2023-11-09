# PHP 설치방법

### php 5
sudo apt-get install php5

### php 7.1
sudo apt-get install apache2 php7.1-curl	

### php 7.2
sudo apt-get install apt-transport-https lsb-release ca-certificates
sudo wget -O /etc/apt/trusted.gpg.d/php.gpghttps://packages.sury.org/php/apt.gpg
sudo echo "debhttps://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list
sudo apt-get update
sudo apt-get install –y php7.2

# 실행방법 
1) comand 창에 /var/www/html/파일명
2) 인터넷 창에 http://localhost/파일명 또는 http://IP/파일명
