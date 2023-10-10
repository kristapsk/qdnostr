#!/usr/bin/env bash

while read -u 3 url; do
    host="$(sed 's/wss:\/\///' <<< "$url")"
    echo -n "$host: "
    if ! nc $host https -w 5; then
        echo "0"
    else
        echo "1"
    fi
done 3< relays.txt
