#!/bin/bash

# should be run as printf "Y\nn\n1\ny\nn" | ./install-hadoop.sh
wget -nv http://public-repo-1.hortonworks.com/ambari/ubuntu14/2.x/updates/2.4.2.0/ambari.list -O /etc/apt/sources.list.d/ambari.list
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
apt-get update
apt-get -y install ambari-server
printf "n\n1\ny\nn" | ambari-server setup
ambari-server start
