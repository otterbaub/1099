# UniFi SSH Manager

  A Terminal User Interface (TUI) application for managing SSH connections to UniFi network devices. Built with Python and Textual, this tool provides an intuitive interface for connecting to
  network equipment across multiple sites.

  ## Features

  - 🌐 **UniFi Integration** - Automatically discovers devices from UniFi Controller
  - 🖥️ **Cross-Platform** - Works on Windows, Linux, and macOS
  - 🔐 **Secure Authentication** - Passwords copied to clipboard for easy access
  - 🌳 **Tree Navigation** - Organized view of sites and devices
  - ⚡ **Quick Connect** - Press Enter to instantly SSH to any device
  - 🔄 **Auto-Restart** - Continue working after SSH sessions end

  ## Screenshots

  📁 SSH Manager
  ├── 📂 Site: Production Network (5 devices)
  │   ├── 🔌 Main-Switch (192.168.1.10) [US-48-500W]
  │   ├── 📡 Office-AP (192.168.1.20) [U6-Pro]
  │   └── 🔌 Secondary-Switch (192.168.1.30) [US-24]
  └── 📂 Site: Guest Network (2 devices)
      ├── 📡 Lobby-AP (192.168.2.10) [U6-Lite]
      └── 🔌 Guest-Switch (192.168.2.20) [US-8]

  ## Installation

  ### Prerequisites
  - Python 3.8+
  - UniFi Controller access
  - SSH client installed on your system

  ### Setup
  1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/unifi-ssh-manager.git
  cd unifi-ssh-manager

  2. Create virtual environment:
  python -m venv ssh-manager-env

  3. Activate virtual environment:
  # Windows
  ssh-manager-env\Scripts\activate

  # Linux/Mac
  source ssh-manager-env/bin/activate

  4. Install dependencies:
  pip install -r requirements.txt

  5. Configure UniFi credentials in ui_ssh_info.py

  Usage

  Run the application:
  python main.py

  Navigation

  - Arrow Keys - Navigate through the tree
  - Enter - Connect to selected device
  - Q - Quit application
  - D - Toggle dark/light mode

  SSH Connection

  1. Navigate to desired device
  2. Press Enter to initiate connection
  3. Password is automatically copied to clipboard
  4. Paste password when prompted by SSH

  Configuration

  Update UniFi Controller settings in ui_ssh_info.py:
  host_address = "your-controller-ip"
  user = "your-username"
  user_pass = "your-password"

  Technical Details

  - Framework: Textual (Modern TUI framework)
  - Architecture: Object-oriented design with Site/Device models
  - Compatibility: Windows, Linux, macOS
  - Dependencies: textual, unificontrol, pyperclip

  Contributing

  1. Fork the repository
  2. Create feature branch (git checkout -b feature/new-feature)
  3. Commit changes (git commit -am 'Add new feature')
  4. Push to branch (git push origin feature/new-feature)
  5. Open Pull Request

  License

  This project is licensed under the MIT License - see the LICENSE file for details.

  Author

  Your Name - Network Engineer & Python Developer

  Acknowledgments

  - Textual framework for excellent TUI capabilities
  - unificontorl library for network device management