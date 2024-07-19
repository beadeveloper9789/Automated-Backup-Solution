import schedule
import time
import subprocess
import os

# Print the current working directory
print("Current directory:", os.getcwd())

# Define the Bash script path
BACKUP_SCRIPT = "/Users/ramnanda/Desktop/s3b.sh"

def run_backup():
    print("Running backup...")
    subprocess.run([BACKUP_SCRIPT])
    print("Upload Successful")
    print("Check S3 Management Console")

# Schedule the backup to run every minute
schedule.every(1).minutes.do(run_backup)

while True:
    schedule.run_pending()
    time.sleep(1)
