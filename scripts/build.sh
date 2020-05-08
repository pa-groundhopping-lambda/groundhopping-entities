#/usr/bin/env bash

zip_name="lib-groundhopping-entites"

[[ "$#" -eq 1 ]] && zip_name="$1"
[[ -d '.temp' ]] && rm -r '.temp'

mkdir '.temp'
cp -r 'schemas' 'requirements.txt' '.temp'

cd '.temp'

pip3 install -r requirements.txt --target . --progress-bar on
rm -rf requirements.txt bin/

mkdir 'python'
mv * 'python'
zip -qr "$zip_name.zip" . && echo "Success: create $zip_name.zip" || echo "Failure: can't zip the project"

cd ..
mv ".temp/$zip_name.zip" .
rm -r '.temp'