sudo apt update && sudo apt upgrade -y
sudo apt install git screen python3 python3-pip python3-venv -y
git clone https://github.com/0xmoei/chatbot-app.git
cd chatbot-app
python3 -m venv venv
source venv/bin/activate
pip install requests
nano chatbot.py
python3 chatbot.py
