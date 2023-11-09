import subprocess


def makemigrations():
    cmd = [
        "python",
        "src/backend/manage.py",
        "makemigrations",
        "core",
        "resume",
        "vacancy",
        "tracker",
        "user",
    ]
    subprocess.run(cmd)


def migrate():
    cmd = ["python", "src/backend/manage.py", "migrate"]
    subprocess.run(cmd)
