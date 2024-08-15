#!/usr/bin/python

import requests
import json


def main():
    url = 'https://api.datadoghq.com/api/v1/dashboard'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DD-API-KEY': '95eb2a9904b69057a4b0407e661de7b2',
        'DD-APPLICATION-KEY': '84818b95e3bb916b2e36cc736273a982e7d80529'
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
