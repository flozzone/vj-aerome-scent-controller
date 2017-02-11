#!/bin/bash

STINKY_USER="root"
STINKY_IP="192.168.1.52"
STINKY_DEPLOY_DIR="/opt/vj-aerome-scent-controller/"
STINKY="$STINKY_USER@$STINKY_IP:$STINKY_DEPLOY_DIR"

scp ./aerome_scent_control_server.py $STINKY
scp ./gpio_stinkomat_6000_controller.py $STINKY
#scp ./requirements.txt $STINKY:~/vj-aerome-scent-controller
scp ./log.ini $STINKY
scp ./vj-aerome-scent-controller.init "$STINKY_USER@$STINKY_IP:/etc/init.d/vj-aerome-scent-controller"

scp -r ./static/ $STINKY

