cp .drone.yml drone_legacy.yml
cp .drone.yml new.yml
convert.py new.yml > secrets.yml
sed -i '1d' secrets.yml
sed -i '$d' secrets.yml
sed -i '1,/kind: secret/!d' new.yml
sed -i 's/kind: secret//' new.yml
sed -i '$d' new.yml
sed -i '$d' new.yml
cat secrets.yml >> new.yml
mv new.yml .drone.yml
rm secrets.yml
git add drone_legacy.yml
