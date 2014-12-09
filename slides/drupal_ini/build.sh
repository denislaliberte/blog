#!/bin/bash

## remove remark specific markdown (slides separator, comments, slides information and todo comments)
sed '/--/d' index.md |  sed '/template:/d' |sed '/class:/d' |sed '/name:/d' | sed '/???/d' | sed '/_todo_/d' > document.md

## build 
#pandoc  -c flatly.css  -o index.html index.md

## build 
pandoc -o document.pdf document.md
