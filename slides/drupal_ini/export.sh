#!/bin/bash

## remove remark specific markdown (slides separator, comments, slides information and todo comments)
sed '/--/d' index.md |  sed '/:/d' | sed '/???/d' | sed '/_todo_/d' > document.md

## export to pdf with pandoc
pandoc -o document.pdf document.md
