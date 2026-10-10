from pathlib import Path
import shutil

def check_root_disk():
    usage = shutil.disk_usage(Path("/"))
    percent = usage.used / usage.total * 100

    if percent >= 90:
        status = "CRITICAL"
    elif percent >= 80:
        status = "WARNING"
    else:
        status = "OK"

    return {
        "check": "root_disk",
        "percent": round(percent, 2),
        "status": status,
    }

if __name__ == "__main__":
    print(check_root_disk())
