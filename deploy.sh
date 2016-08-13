#!/bin/bash

scp ./aerome_scent_control_server.py pi@192.168.1.141:~/vj-aerome-scent-controller/
scp ./gpio_stinkomat_6000_controller.py pi@192.168.1.141:~/vj-aerome-scent-controller/
scp ./requirements.txt pi@192.168.1.141:~/vj-aerome-scent-controller
scp ./log.ini pi@192.168.1.141:~/vj-aerome-scent-controller

scp -r ./static/ pi@192.168.1.141:~/vj-aerome-scent-controller/
