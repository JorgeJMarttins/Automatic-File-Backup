import os
import shutil
import time
from datetime import datetime

# Function to perform the backup of files
def backup_files(source, destination):
    # Create a timestamp for the backup name (e.g., 20241214_153000)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Define the backup directory name, including the timestamp
    backup_destination = os.path.join(destination, f'backup_{timestamp}')
    
    # Copy the folder or files to the backup destination
    shutil.copytree(source, backup_destination)
    
    # Print a confirmation message after the backup is done
    print(f'Backup completed successfully to {backup_destination}')

# Function to perform backups automatically at regular intervals
def automatic_backup(source, destination, interval_seconds):
    while True:
        # Perform the backup by calling the backup_files function
        backup_files(source, destination)
        
        # Print a message indicating the waiting period before the next backup
        print(f'Waiting {interval_seconds} seconds for the next backup...')
        
        # Wait for the specified interval before performing the next backup
        time.sleep(interval_seconds)

# Path to the directory or file to be copied
source = 'path/to/your/source_directory_or_file'  # Replace with your source path

# Path to the directory where the backup will be stored
destination = 'path/to/your/backup_directory'  # Replace with your destination path

# Time interval between backups (in seconds). E.g., 3600 seconds = 1 hour.
interval_seconds = 3600

# Start the automatic backup process by passing the source and destination paths and the time interval
automatic_backup(source, destination, interval_seconds)
