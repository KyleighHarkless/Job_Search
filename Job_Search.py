import csv
from Job_Class import Job_Class

def main():
    create_jobs_list("fake_jobs.csv")

def create_jobs_list(filename: str):
    list_of_jobs = []

    try:
        with open(filename, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                if len(row) >= 4:
                    job = Job_Class(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip())
                    list_of_jobs.append(job)

        print(f"Total jobs loaded: {len(list_of_jobs)}")
        for job in list_of_jobs:  
            print(job)

    except FileNotFoundError:
        print("Could not find 'fake_jobs.csv'. Make sure it's in the same folder as this script.")
    except Exception as e:
        print(f"Error: {e}")

def search_jobs(keyword: str, location: str):
    results = []
    return results

if __name__ == "__main__":
    main()