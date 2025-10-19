import csv
from Job_Class import Job_Class
from datetime import datetime

def main():
    available_jobs = create_jobs_list("fake_jobs.csv")

    choice = input("Job Search: \n(1) View all jobs postings\n"
    "(2) View most recent job postings \n"
    "(3) Search jobs by keyword and location? \n" \
    "Enter 1, 2, or 3: ")

    job_menu(choice, available_jobs)

def job_menu(choice: str, jobs_list: list):
    if choice == "1":
        for job in jobs_list:
            print(job)

    elif choice == "2":
        ordered_jobs = order_jobs_by_date(jobs_list)
        for job in ordered_jobs:
            print(job)

    elif choice == "3":
        keyword = input("Enter keyword to search for: ")
        location = input("Enter location to search for: ")
        search_results = search_jobs(jobs_list, keyword, location)
        for job in search_results:
            print(job)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


def create_jobs_list(filename: str):
    list_of_jobs = []

    try:
        with open(filename, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if len(row) >= 4:
                    job = Job_Class(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip())
                    list_of_jobs.append(job)

            return list_of_jobs
        
    except FileNotFoundError:
        print("Could not find file.")

def order_jobs_by_date(jobs_list: list):
    most_recent = []
    sorted_by_date = sorted(jobs_list, key=lambda job: job.date_posted, reverse=True)

    for job in sorted_by_date:
        if job.date_posted[:4] == datetime.now().year:
            most_recent.append(job)

    return most_recent



def search_jobs(jobs_list: list, keyword: str, location: str):
    results = []
    for job in jobs_list:
        if keyword.lower() in job.title.lower() and location.lower() in job.location.lower():
            results.append(job)

    return results

if __name__ == "__main__":
    main()