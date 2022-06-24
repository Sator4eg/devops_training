#!/bin/bash
ls -alR /usr | grep "^...x" | grep -v "^d" > executable.txt


