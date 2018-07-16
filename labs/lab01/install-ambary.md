# Установка Ambary
```
git clone https://github.com/newprolab/content_bigdata8.git
cd content_bigdata8/labs/lab01
chmod +x install-hadoop.sh
``` 
Отправляем нужные скрипты на клауд:
```
scp -i npl.pem install-hadoop.sh ubuntu@<your_server_manager_public_dns>:/home/ubuntu/.
```

Логинимся через SSH на <server_manager_public_dns>
Затем:
```
sudo su
./install-hadoop.sh
```
