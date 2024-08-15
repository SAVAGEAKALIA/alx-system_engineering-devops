#!/usr/bin/python

import requests
import json
import os


def main():
    url = 'https://api.datadoghq.com/api/v1/dashboard'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DD-API-KEY': os.getenv('DD-API-KEY'),
        'DD-APPLICATION-KEY': os.getenv('DD-APPLICATION-KEY')
    }

    req = requests.get(url, headers=headers, allow_redirects=False)
    print(req.status_code)
    print(json.dumps(req.json(), indent=4))
    if req.status_code == 200:
        dashboards = req.json()['dashboards']
        print(dashboards[0]['id'])
        return dashboards[0]['id']
        # for dashboard in dashboards:
        #     if dashboard['title'] == "Saviour's Web-01 Monitoring Dashboard":
        #         print(dashboard['id'])
        #         break


if __name__ == '__main__':
    dashboard_id = main()

    if dashboard_id is not None:
        with open("2-setup_datadog", 'w') as file:
            file.write(dashboard_id)
