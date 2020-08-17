#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export dir=$DIR'/utils'

python3 manage.py shell < ./utils/db.py