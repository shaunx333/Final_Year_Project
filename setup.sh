root=$(pwd)
printf "\n\n#####   Updating stuff   ####\n\n"
sudo apt-get update -y

pub_ip=$(dig +short myip.opendns.com @resolver1.opendns.com)

printf "\n\n#####   Cloning repo   ####\n\n"

printf "#####   Appending to ALLOWED_HOSTS: "+$pub_ip
sed -i "s/'127.0.0.1'/'127.0.0.1', '$pub_ip'/g" $root/untitled1/settings.py

printf "\n\n#####   Installing Python & Prerequisite    ####\n\n"
sudo apt install -y python3-pip sqlite3 libsqlite3-dev
sudo apt install -y jpegoptim optipng
sudo pip3 install virtualenv
python3 -m pip install --upgrade pip

printf "\n\n#####   Installing Virtual Env   ####\n\n"
virtualenv -p $(which python3) $root/venv

printf "\n\n#####   Installing these packages:   ####\n\n"
cat $root/requirements.txt
pip3 install -r $root/requirements.txt > /dev/null
printf "Done"

printf "\n\n"
read -p "Turn server live?: press 'y' for yes, any other to exit:  "  choice
if [ "$choice" != "" ] && [ $choice = y ];
then
  source venv/bin/activate
  bash m.sh
else
  echo "Cool"
fi
