chmod u+x start.sh
echo 'start install requirements'
pip install -r requirements.txt
echo 'start server'
python3 server.py