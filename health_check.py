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


def check_memory():
    meminfo = Path("/proc/meminfo").read_text(encoding="utf-8")
    values = {}

    for line in meminfo.splitlines():
        key, value = line.split(":", 1)
        values[key] = int(value.strip().split()[0])

    total = values["MemTotal"]
    available = values["MemAvailable"]
    used_percent = (total - available) / total * 100

    if used_percent >= 90:
        status = "CRITICAL"
    elif used_percent >= 80:
        status = "WARNING"
    else:
        status = "OK"

    return {
        "check": "memory",
        "used_percent": round(used_percent, 2),
        "status": status,
    }


if __name__ == "__main__":
    print(check_root_disk())
    print(check_memory())
