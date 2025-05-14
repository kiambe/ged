#!/bin/bash

# Navigate to the directory where your Django app is located
#cd /path/to/your/django/project
cd /root/ged/
# Activate your virtual environment (adjust the path if necessary)
source ged_env/bin/activate

# Run Django migrations (optional, only if required)
#python manage.py migrate

cd /root/ged/ged_backend

# Start Django using PM2
pm2 start --only "python manage.py runserver 0.0.0.0:8000" --name ged_pm2_app

# Save the PM2 process list to ensure it restarts on system reboot
pm2 save

# Optionally, enable PM2 to restart your app on system reboot
pm2 startup

echo "Django app is running using PM2!"
