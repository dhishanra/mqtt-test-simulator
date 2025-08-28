## Installation

Run the following command to install dependencies:

```bash
sudo apt update && sudo apt install -y python3-paho-mqtt


## Run Multiple Publishers

To start 10 publisher instances in the background, run:

```bash
for i in {1..10}; do python3 mqtt_publisher.py & done
