#!/bin/bash 
chmod u+x pubs.py
chmod u+x subs.py

pip install paho-mqtt
pip install influxdb

docker exec -it grafana grafana-cli plugins install natel-plotly-panel
docker restart grafana

./subs.py
