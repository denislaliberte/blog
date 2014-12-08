#!/bin/bash

## remove remark specific markdown
sed '/--/d' index.md |  sed '/:/d' | sed '/???/d' > document.md

## expoert to pdf with pandoc
pandoc -o document.pdf document.md
