#!/bin/bash
# networking 
curl -sI "$1" | grep "Allow" | cut -d  " " -f 2- 
