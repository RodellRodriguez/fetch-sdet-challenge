# fetch-sdet-challenge
Coding challenge from Fetch for the SDET position.

Requirements to execute this code:
 - Linux os
 - Python version `3.8+` is installed
 - `venv` is installed, otherwise `run.sh` will fail
 - Google Chrome web browser version `127`, which is the latest stable version of Google Chrome at the time of creation of this project, otherwise the Chrome web browser will fail to open.

Project Breakdown:
 - Python Script (.py file): Your main Selenium script that automates opening the browser and performing the browser actions.
 - Requirements File (requirements.txt): A file listing all the Python dependencies needed to run the script.
 - Driver Executable: The web driver (chromedriver for the Chrome browser) that Selenium uses to control the browser. We are using ChromeDriver version `127.0.6533.99`, which is the latest version as of the time of creation of this project.
 - Executable Script (run.sh or run.bat): A script to automate the setup and execution process.

Steps to run the program:
1. Make `run.sh` executable by running the command `chmod +x run.sh`
2. Run the project: `./run.sh`

