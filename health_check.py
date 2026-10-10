def check_memory():
    meminfo = Path("/proc/meminfo").read_text(encoding="utf-8")
    values = {}

    for line in meminfo.splitlines():
        key, value = line.split(":", 1)
        values[key] = int(value.strip().split()[0])

    total = values["MemTotal"]
    available = values["MemAvailable"]
    used_percent = (total - available) / total * 100

    return {
        "check": "memory",
        "used_percent": round(used_percent, 2),
    })
