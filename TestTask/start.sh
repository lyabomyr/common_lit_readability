chmod u+x start.sh

echo 'start script wait 5s'
pip install -r requirements.txt
echo 'start ML'

python3 Readability/main.py > metrix.txt
echo 'create folder with result metrix'



[[ -f $PWD ]] && echo "$FILE exists."

[ ! -d "$PWD/result" ] && echo mkdir result
[ "$(ls -A $PWD/result)" ] && rm -v /$PWD/result/* || echo "Empty"

mv -v metrix.txt /$PWD/result
mv -v *.png /$PWD/result
mv -v submission.csv /$PWD/result
