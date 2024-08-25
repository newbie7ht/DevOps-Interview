#!/bin/bash

# Define log file path and archive path
LOGFILE="/var/log/myapp/app.log"
ARCHIVE_DIR="/var/log/myapp/archive"

# Create the archive directory if it doesn't exist
mkdir -p $ARCHIVE_DIR

# Get the current date
DATE=$(date +"%Y%m%d")

# Archive the log file
mv $LOGFILE $ARCHIVE_DIR/app_$DATE.log

# Create a new log file
touch $LOGFILE

# Set correct permissions
chmod 644 $LOGFILE

# Restart the application to use the new log file (optional)
# systemctl restart myapp

echo "Log rotation completed."
