import datetime


def create_calendar_file():
    """
    Create a file called `calendar.txt` and save it in the current directory.
    The file should contain the menstrual cycle data in the following format:

    start_date,end_date
    2023-01-01,2023-01-08
    2023-02-01,2023-02-07
    ...

    """

    with open("calendar.txt", "w", encoding="utf-8") as f:
        for i in range(1, 12):
            start_date = datetime.date(2023, i, 1)
            end_date = start_date + datetime.timedelta(days=7)
            f.write(f"{start_date}, {end_date}\n")


if __name__ == "__main__":
    create_calendar_file()
