#!/bin/bash
string=`pwd`
echo $string
if [[ $string == *"/root"* ]]; then
  echo "You are at the right place!"
else
  echo "Go away!"
fi

