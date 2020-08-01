copy Bale.sh => /lib/zabbix/alertscripts/
pip3 install -r requirements.txt
# run python script to get chat id and copy to user profile in zabbix
python3.6 sendbaleBot.py
