#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
curl -sI GET "$1" | grep -i "Content-length" | cut -d" " -f2
