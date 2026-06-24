from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Tree
from .models import Site, Device



host_address = "192.168.0.44"
user = "otterbaub"
user_pass = "7232Siena92683CA!"

class SSHManagerTUI(App):
    """ A Textual TUI App for SSH connections"""
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("q", "quit", "Quit the app"),
                ]
    
    def __init__(self):
        super().__init__()
        self.restart_callback = None

    def set_restart_callback(self, callback):
        self.restart_callback = callback

    def action_quit(self):

        if self.restart_callback:
            self.restart_callback(False)
        self.exit()


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        tree = Tree("SSH Manager")
        tree.root.expand()
        self.populate_tree(tree)
        yield tree
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def populate_tree(self, tree: Tree):
        try:
            # Suppress unificontrol warnings
            import warnings
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            import sys
            import os
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sys.path.insert(0, parent_dir)

            import ui_ssh_info
            raw_data = ui_ssh_info.get_ssh_info(host_address, user, user_pass)

            for site_name, site_data in raw_data.items():
                devices = []
                for device_data in site_data['device_list']:
                    device = Device(
                        device_data['device_name'],
                        device_data['device_ip'],
                        device_data['device_mac'],
                        device_data['device_model'],
                        device_data['device_type']
                    )
                    devices.append(device)

                site = Site(
                    site_name,
                    site_data['ssh_user'],
                    site_data['ssh_pass'],
                    devices
                )
                site_node = tree.root.add(str(site))
                site_node.data = site

                for device in site.devices:
                    device_node = site_node.add_leaf(str(device))
                    device_node.data = device

        except Exception as e:
            # Fallback test data if UniFi connection fails
            device1 = Device("Test-Switch", "192.168.0.92", "aa:bb:cc", "Test", "test")
            site1 = Site("Test Site", "admin", "password", [device1])

            site_node = tree.root.add(str(site1))
            site_node.data = site1

            for device in site1.devices:
                device_node = site_node.add_leaf(str(device))
                device_node.data = device
    
    def on_tree_node_highlighted(self, event):
        """"Handle when a tree node is highlighted/selected"""
        self.current_selection = event.node

    def on_tree_node_selected(self, event):
        """Handle tree node selection."""
        print("DEBUG: Tree node selected with Enter!")
        node = event.node
        print(f"DEBUG: Selected node: {node}")

        if hasattr(node, 'data') and isinstance(node.data, Device):
            print("Debug: It's a device!")
            device = node.data
            site = node.parent.data
            ssh_command = device.get_ssh_commands(site.ssh_user, site.ssh_pass)
            print(f"DEBUG: SSH command: {ssh_command}")
            self.launch_ssh(ssh_command)
    
    def launch_ssh(self, ssh_command):
        import subprocess
        import pyperclip
        import platform

        # Copy password to clipboard for all platforms
        site = self.current_selection.parent.data
        pyperclip.copy(site.ssh_pass)

        os_type = platform.system().lower()

        if os_type == "windows":
            # Windows: Use PowerShell
            self.call_after_refresh(self._launch_ssh_after_exit, ssh_command, "windows")
        elif os_type in ["linux", "darwin"]:  # darwin = macOS
            # Linux/Mac: Use terminal
            self.call_after_refresh(self._launch_ssh_after_exit, ssh_command, "unix")
        else:
            # Unknown OS - fallback to basic
            self.call_after_refresh(self._launch_ssh_after_exit, ssh_command, "basic")

        self.exit()

    def _launch_ssh_after_exit(self, ssh_command, os_type):
        """Helper method to launch SSH after TUI exits"""
        import subprocess

        try:
            if os_type == "windows":
                # Windows: Run in current terminal
                subprocess.run(ssh_command, shell=True)
            elif os_type == "unix":
                # Linux/Mac: Run in current terminal
                subprocess.run(ssh_command, shell=True)
            else:
                # Basic fallback
                subprocess.run(ssh_command, shell=True)

        except Exception as e:
            print(f"Error launching SSH: {e}")

        print(f"\nSSH session ended on {os_type} system.")
        print("Password was copied to clipboard for easy pasting.")

        restart = input("Restart SSH Manager? (y/n): ")
        if self.restart_callback:
            self.restart_callback(restart.lower() in ['y', 'yes'])


if __name__ == "__main__":
    app = SSHManagerTUI()
    app.run()