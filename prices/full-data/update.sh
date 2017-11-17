#!/home/stan/Desktop/Crypto/update.sh

git add --all
git commit -m "update: $(date +"%B-%d-%y")"
git push origin master