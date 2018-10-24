import os, sys
import sched
import time, datetime
import subprocess
try:
    import schedule
except ImportError:
    print("schedule libraryが未インストールです.\n'pip install schedule'を実行し、インストールしてください。'")
    sys.exit(1)

os.chdir("/home/ec2-user/discord_bot")

cmd = "nohup python discord_bot.py >> bot.out &"

def job():
    with open("pid.txt", "r", encoding="utf-8") as f:
        pid = f.read()
        subprocess.Popen(["kill", pid.strip("\n")])
    proc = subprocess.Popen(cmd.split())
    with open("pid.txt", "w", encoding="utf-8") as f:
        f.write(str(proc.pid))
    del f
    del pid

# 必要に応じてscheduleの前の「#」をつけたり外したりしてください。
# 毎日午前3時(JST)にプログラムを自動再起動
schedule.every().day.at("3:00").do(job)

# 毎週月曜日午前3時にプログラムを自動再起動
#schedule.every().monday.at("3:00").do(job)

# 10日ごとに午前3時にプログラムを自動再起動
#schedule.every(10).days.at("3:00").do(job)

proc = subprocess.Popen(cmd.split())
with open("pid.txt", "w", encoding="utf-8") as f:
    f.write(str(proc.pid))
del f

while True:
    schedule.run_pending()
    time.sleep(1)
