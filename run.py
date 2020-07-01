# coding: utf8

import os
import csv
import time
import argparse
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



path = Path(__file__).parent / 'polling_stations'
try:
    path.mkdir()
except:
    pass


class Election:
    def make_polling_stations_dir(self, name):
        path = Path(__file__).parent / 'polling_stations' / name
        try:
            path.mkdir()
        except:
            pass
 
    def make_cam_dir(self, name, cam):
        path = Path(__file__).parent / 'polling_stations' / name / str(cam+1)
        try:
            path.mkdir()
        except:
            pass
        return path

    def get_series(self, path) -> int:
        files = os.listdir(path)
        if files:
            files_serieses = sorted([s.split('_')[0] for s in files])
            return int(files_serieses[-1]) + 1
        return 1

    def start(self, stream_delay, shots_delay, stations_path):
        with open(stations_path) as stations_file:
            stations = []
            for i in stations_file.readlines():
                stations.append(i.rstrip())

        with open('webcams.csv', 'r', encoding='utf8') as f:
            polling_stations = csv.DictReader(f)
            polling_stations = filter(lambda x: x['number'] in stations, polling_stations)

            driver = webdriver.Chrome()

            for polling_station in polling_stations:
                if polling_station['kind'] == 'УИК':
                    name = polling_station['number']
                    id_ = polling_station['id']
                    self.make_polling_stations_dir(name)
                    for cam in range(2):
                        path = self.make_cam_dir(name, cam)
                        driver.get(f'https://vybory.mos.ru/voting-stations/{id_}?channel={cam}')
                        while True:
                            try:
                                element_present = expected_conditions.presence_of_element_located((By.CLASS_NAME,
                                                                                                   'zGgQYFH7FOF05jHEbOfau'))
                                WebDriverWait(driver, 5).until(element_present)
                                break
                            except:
                                input('Введите капчу в браузере и нажмите Enter в консоли')

                        driver.execute_script("window.localStorage.clear();")
                        elem = driver.find_elements_by_css_selector('video')[0]
                        elem_parent = elem.find_element_by_xpath('..')
                        elem_buttons = elem_parent.find_elements_by_xpath('//button')
                        elem_buttons[4].click()
                        # elem = driver.find_element_by_class_name('zGgQYFH7FOF05jHEbOfau')
                        # elem.click()
                        time.sleep(stream_delay)
                        series = self.get_series(path)
                        for i in range(3):
                            current_time = datetime.now().strftime('%H_%M_%S')
                            driver.save_screenshot(str(path / f'{series}_{i+1}_{current_time}.png'))
                            time.sleep(shots_delay)
                        driver.execute_script("window.localStorage.clear();")
                        driver.execute_script("window.sessionStorage.clear();")
                        driver.delete_all_cookies()
                        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stream_delay', type=int, default=2)
    parser.add_argument('--shots_delay', type=int, default=5)
    parser.add_argument('--stations', default='stations.txt')
    args = parser.parse_args()
    election = Election()
    election.start(args.stream_delay, args.shots_delay, args.stations)
