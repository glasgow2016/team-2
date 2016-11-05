#!/bin/bash
cd ~/team-2/
if git pull | grep -q 'Unpacking' ; then
    echo Updated
    kill -9 $(pidof python)
    (python ~/team-2/Maggies_Center/manage.py runserver 0.0.0.0:8000 &>/dev/null) &disown
    echo Finished!
else
    echo Not updated
fi

