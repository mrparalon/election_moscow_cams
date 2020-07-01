import argparse
import os
import json
from pathlib import Path

with open('minimal.json') as f:
    cam_ids = json.load(f)
    cam_ids = {str(v['number']): v for v in cam_ids}


parser = argparse.ArgumentParser()
parser.add_argument('region')
args = parser.parse_args()

path = Path(__file__).parent / args.region

station_names = os.listdir(path)
for station_name in station_names:
    station_path = path / station_name
    for cam in range(2):
        cam_path = station_path / str(cam+1)
        files = os.listdir(cam_path)
        for file_name in files:
            file_path = cam_path / file_name
            new_name = file_name.split('.')[0]
            new_name = new_name.replace('_', '-')
            new_name = new_name.replace('-', '_', 2)
            new_name = f'{new_name}.png'
            file_path.rename(cam_path / new_name)
        station_obj = cam_ids.get(station_name)
        if station_obj is not None:
            cam_uuid = station_obj['cameras'][cam]['uuid']
            cam_path.rename(cam_path.parent / cam_uuid)


