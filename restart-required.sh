#!/bin/bash
if [ -f /var/run/reboot-required ]; then
  echo 'Reboot required'
else
  echo 'Reboot NOT required'
fi
