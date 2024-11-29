#! /usr/bin/bash

echo "CAUTION! Do not use this script if you need more than one version of node!"
while true; do
    read -p "You want to start this script? (Y/n): " choice
    if [[ "$choice" == "Y" || "$choice" == "y" ]]; then
        echo "Node Version Fix script started. Verifying your version..."
        break
    elif [[ "$choice" == "N" || "$choice" == "n" ]]; then
        echo "Script terminated."
        exit 0
    else
        echo "Invalid input, retry."
    fi
done

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

pre_long_bnode=$(which node)
pre_bnode=$(echo "$pre_long_bnode" | sed 's/\/bin\/node$//')
old_version=$(echo "$pre_long_node" | grep -o 'v[0-9]\+\.[0-9]\+\.[0-9]\+')

nvm install node

post_long_node=$(which node)
new_version=$(echo "$post_long_node" | grep -o 'v[0-9]\+\.[0-9]\+\.[0-9]\+')

if [ "$old_version" != "$new_version" ] && [ "$pre_bnode" != "" ] ; then
    echo "Bugged node version detected, applying the fix..."
    nvm alias default "$new_version"
    rm "$pre_bnode" -r
    echo "Node fixed, enjoy!"
else
    echo "Your node version is already the latest one, it needs no fix!"
fi