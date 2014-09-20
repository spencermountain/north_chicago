sudo apt-get install openvpn

cd bloomberg

sudo cp bloomberg_api.ovpn /etc/openvpn/bloomberg_api.conf
sudo cp bloomberg.crt /etc/openvpn
sudo cp hack_the_north_fall_2014_* /etc/openvpn

sudo service openvpn reload
