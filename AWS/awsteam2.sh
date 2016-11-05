#!/bin/bash
if [ -z ${TEAM2KEYLOCATION+x} ]; then echo "Please export TEAM2KEYLOCATION=/some/dir/file.pem"; else
ssh -i $TEAM2KEYLOCATION force@ec2-52-18-198-15.eu-west-1.compute.amazonaws.com
fi