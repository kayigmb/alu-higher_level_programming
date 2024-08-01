#!/bin/bash
# networking
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
