import random
import subprocess
import re

# Rastgele MAC adresi oluştur
charList = "0123456789ABCDEF"
newMac = ":".join(["".join(random.choices(charList, k=2)) for _ in range(6)])

# Eski MAC adresini al
try:
    ifconfigResult = subprocess.check_output("ip link show enp12s0", shell=True).decode()
    oldMacMatch = re.search(r"link/ether ([\da-fA-F:]{17})", ifconfigResult)
    if oldMacMatch:
        oldMac = oldMacMatch.group(1)
    else:
        raise ValueError("MAC adresi bulunamadı.")
except Exception as e:
    print(f"Hata: {e}")
    exit(1)

# MAC adresini değiştir
try:
    subprocess.check_output("ip link set dev enp12s0 down", shell=True)
    subprocess.check_output(f"ip link set dev enp12s0 address {newMac}", shell=True)
    subprocess.check_output("ip link set dev enp12s0 up", shell=True)
except Exception as e:
    print(f"Hata: {e}")
    exit(1)

print(f"Old MAC address: {oldMac}")
print(f"New MAC address: {newMac}")
