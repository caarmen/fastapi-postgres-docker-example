#!/bin/bash
if [ "$DEBUG" = "debugpy" ]
then
  echo "Running in debug mode"
  pip install debugpy -t /tmp
  python /tmp/debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:server --host 0.0.0.0 --port 8000 --reload
elif [ "$DEBUG" = "pdb" ]
then
  echo "Running with PDB"
  pip install web-pdb
  uvicorn app.main:server --host=0.0.0.0 --reload
else
  echo "Running in production mode"
  uvicorn app.main:server --host=0.0.0.0 --reload
fi