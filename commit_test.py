import datetime
import subprocess


def make_git_init():
    git_init = ["git", "init"]
    subprocess.run(git_init, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def make_git_add():
    git_add = ["git", "add", "."]
    subprocess.run(git_add, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def make_git_commit():
    git_commit = ["git", "commit", "-m", "commit"]
    subprocess.run(git_commit, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def change_commit_date(year, month, day):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    date = datetime.date(year, month, day)
    weekday = weekdays[date.weekday()]
    commit_time = f"{weekday} {months[month - 1]} {day} 12:34:56 {year} +0900"
    command = ["git", "commit", "--amend", "--no-edit", f"--date=\"{commit_time}\""]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    command = ["git", "rebase", "HEAD~1", "--committer-date-is-author-date"]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def make_time_git_commit(d):
    make_git_add()
    make_git_commit()
    change_commit_date(d.year, d.month, d.day)


def main():
    year = 2022
    month = 11
    day = 11
    d = datetime.date(year, month, day)
    make_time_git_commit(d)


if __name__ == "__main__":
    main()
