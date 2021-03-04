import os
from random import randint
from datetime import datetime, timedelta

start_date = datetime(2021, 3, 1)  # Set your start date
end_date = datetime(2021, 6, 28)   # Set your end date

commits_per_day = 1  # Number of commits per day
gap_range = (1, 7)   # Range for the gap between commits (in days)

current_date = start_date

while current_date <= end_date:
    for _ in range(commits_per_day):
        gap = randint(*gap_range)
        commit_date = current_date + timedelta(days=gap)

        if commit_date > end_date:
            break

        d = commit_date.strftime("%Y-%m-%d %H:%M:%S") + " days ago"
        
        with open('file.txt', 'a') as file:
            file.write(d + "\n")
        
        os.system('git add .')
        os.system(f'git commit --date="{commit_date.strftime("%a %b %d %H:%M:%S %Y")}" -m "Commit on {d}"')
        os.system('git push -u origin main')

    current_date += timedelta(days=1)