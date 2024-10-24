# Giovanni Android Framework
*Final Year Project, May 2024*  
*Author: John S. Madaha*  
*Email: [johnmadaha6@gmail.com](mailto:johnmadaha6@gmail.com)*  
![Screenshot from 2024-10-24 13-02-14](https://github.com/user-attachments/assets/3c2f7cb7-fba4-4a1a-a82d-2253b7dd0720)


## Overview

The **Giovanni Android Framework** is an exploitation framework designed for remote access and interaction with Android devices. This Python-based tool allows users to connect to Android devices, execute commands, and perform various administrative tasks, including capturing screenshots, pulling files, and managing applications remotely.

The framework simplifies interaction with Android devices using **ADB (Android Debug Bridge)** and is equipped with an autocompletion feature for improved user experience. This project is a culmination of my final year efforts to create a flexible, user-friendly, and feature-rich tool for Android administration and testing.

## Features

- **Connect and manage Android devices** via ADB over TCP/IP.
- **Interactive command-line interface** with autocompletion for actions.
- **Remote control and monitoring**, including:
  - Device shell access.
  - Pulling files, installing APKs, and taking screenshots.
  - Recording screen activities.
  - Extracting device information and logs.
  - Simulating button presses and performing other administrative tasks.

## Command List

Some of the primary actions available in the framework include:

1. Show connected devices.
2. Disconnect all devices.
3. Connect a new device using an IP address.
4. Access the device's shell.
5. Install an APK on a device.
6. Record the screen.
7. Get a device screenshot.
8. Restart the Giovanni Server.
9. Pull files from the device.
10. Shutdown the device.
11. # etc......

Additional functionalities, such as **Bluetooth interaction**, **GPS spoofing**, **live log monitoring**, and **screen mirroring**, are still under development.

For a complete list of commands, refer to the following:
```plaintext
1 - Show connected devices       10 - Shutdown the device      19 - Extract APK from app      28 - Call a specific number
2 - Disconnect all devices       11 - Uninstall an app         20 - Get Battery Status        29 - Get a Location
3 - Connect a new device         12 - Show device log          21 - Get Network Status        30 - Get camera to take a photo
4 - Access device shell          13 - Dump System Info         22 - Turn WiFi on/off          31 - Start a keylogger
5 - Install an APK on a device   14 - List all device apps     23 - Remove device password    32 - Record Audio
6 - Screen record a device       15 - Run a device app         24 - Emulate button presses    33 - Get SMS
7 - Get device screenshot        16 - Port Forwarding          25 - Get Current Activity      34 - Get Browser History
8 - Restart Giovanni Server      17 - Grab wpa_supplicant      26 - Update Giovanni Framework 35 - Clipboard Hijacking
9 - Pull files from device       18 - Show Mac/Inet            27 - Exit Giovanni Framework   36 - Toggle Flashlight
```

## Installation & Usage

To run the Giovanni Android Framework, you need to have Python 3.x and ADB installed on your system.

### Prerequisites

- Python 3.x
- ADB (Android Debug Bridge)

### Running the Framework

1. Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/GiovanniJohnArthur/FinalYearProject.git
   cd FinalYearProject
   ```

2. Ensure ADB is running in TCP/IP mode:

   ```bash
   adb tcpip 5555
   ```

3. Run the Giovanni Android Framework:

   ```bash
   ./giovanni_framework.py
   ```

4. Use the framework's interactive menu to perform the desired actions on connected Android devices.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file in the repository.

## Future Work

- Implement features for **Bluetooth interaction**, **GPS spoofing**, **live log monitoring**, and **screen mirroring**.
- Improve the user interface and add a web-based control panel.

## Contact

For any questions or suggestions, feel free to contact me at [johnmadaha6@gmail.com](mailto:johnmadaha6@gmail.com).
```

This `.md` file provides a structured format to explain your project and guide users on how to use it. You can further expand it depending on additional details you want to include.
