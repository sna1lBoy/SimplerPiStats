import subprocess
import time
from flask import Flask, render_template
import waitress

app = Flask(__name__)

@app.route('/')
def index():
    # get output
    hostname = subprocess.check_output(['hostname']).decode().strip()
    cpu_lookup = subprocess.Popen(["top", "-n", "1", "-b"], stdout=subprocess.PIPE, text=True)
    time.sleep(.1)
    for line in cpu_lookup.communicate()[0].split("\n"):
        if line.startswith("%Cpu(s)"):
            cpu = round(100 - float(line.split(",")[3].strip().replace("id", "")), 2)
    if cpu <= 40:
        cpu_status = "happy"
    elif cpu <= 74:
        cpu_status = "neutral"
    else:
        cpu_status = "angry"

    # 0 - 40 :]
    # 41 - 74 :|
    # 75 - 100 >:[
    
    temp_lookup = subprocess.Popen(["/usr/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE, text=True)
    time.sleep(.1)
    for line in temp_lookup.communicate()[0].split("\n"):
        if line.startswith("temp="):
            temp = float(line.lstrip("temp=").rstrip("'C"))
            Celsius = temp
    if Celsius <= 50:
        temp = "1"
    elif Celsius <= 70:
        temp = "2"
    else:
        temp = "3"
    return render_template("SimplerPiStats.html", hostname=hostname, cpu_status=cpu_status, cpu_status_numbers=str(cpu) + "%", temp=temp, Celsius=str(Celsius) + "°C")

ip_addresses = subprocess.check_output(['hostname', '-I']).decode().strip().split(" ")
print(f"\033[0;32mSimple\033[0;92mr\033[0m\033[0;32mPiStats is currently running on http://{ip_addresses.pop(0)}:{5556}")

waitress.serve(app, host="0.0.0.0", port=5556)
