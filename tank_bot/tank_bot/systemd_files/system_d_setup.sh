#!/bin/bash

# this moves file into systemd.
sudo cp tank_bot/tank_bot/systemd_files/tank_bot.service /etc/systemd/system/tank_bot.service

# this enables tank_bot to run at boot.
sudo systemctl enable tank_bot.service