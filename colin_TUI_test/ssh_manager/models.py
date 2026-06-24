class Device:
    def __init__(self, name, ip, mac, model, device_type):
        self.name = name
        self.ip = ip
        self.mac = mac
        self.model = model
        self.device_type = device_type

    def __str__(self):
        return f"{self.name} ({self.ip})"

    def get_ssh_commands(self, ssh_user, ssh_pass):
        return f"ssh {ssh_user}@{self.ip}"
    

class Site:
    def __init__(self, name, ssh_user, ssh_pass, devices, firewall_ip=None):
        self.name = name
        self.ssh_user = ssh_user
        self.ssh_pass = ssh_pass
        self.devices = devices if devices is not None else []

    def __str__(self):
        return f"Site: {self.name} with {len(self.devices)} devices"
    
    def add_device(self, device):
        """ add a device to this site"""
        self.devices.append(device)

if __name__ == "__main__":
    device = Device("Switch-01", "192.168.1.10", "aa:bb:cc", "US-48", "switch")
    site = Site("Test Site", "admin", "password", [device])
    print(device)
    print(site)
    print(device.get_ssh_commands("admin", "password"))