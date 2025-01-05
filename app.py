import os
from random import randint
from datetime import datetime, timedelta

# Set the start and end dates for the commits
start_date = datetime(2021, 3, 1)
end_date = datetime(2021, 1, 31)

# Generate commits between January and March 2023
for i in range(1, 10):
    for j in range(0, randint(1, 10)):
        # Calculate the date of the commit based on the range of days
        commit_date = start_date + timedelta(days=i)
        if commit_date > end_date:
            break
        
        # Create a commit message and format the date
        d = commit_date.strftime("%Y-%m-%d %H:%M:%S") + " days ago"
        
        with open('file.txt', 'a') as file:
            file.write(d + "\n")
        
        # Add the changes, commit with a unique message, and push
        os.system('git add .')
        os.system(f'git commit --date="{commit_date.strftime("%a %b %d %H:%M:%S %Y")}" -m "Commit on {d}"')
        os.system('git push -u origin main')
