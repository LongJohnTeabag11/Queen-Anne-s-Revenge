from Recorder import main1
from Converter import main2
import subprocess

try:
    subprocess.run(["mkdir", "-p", "MPTHREE"], check=True)
except:
    pass
main1()
main2()
