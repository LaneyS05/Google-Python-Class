import shutil
import psutil

du = shutil.disk_usage("/")
du.free/du.total*100
print(du)

print(psutil.cpu_percent(0.1))