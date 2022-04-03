#!/bin/bash
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $DIR
source .venv/bin/activate
python qr_code_checker.py
