import subprocess

def ping_(ip, param):
    result = subprocess.run(['ping', param, "4", ip], capture_output=True, text=True)
    result = result.stdout
    if "TTL=" in result:
        return True
    else:
        return False