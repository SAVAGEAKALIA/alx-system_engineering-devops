#!/usr/bin/python

import requests
import json
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi


def dash_id():
    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        dashboards_api = DashboardsApi(api_client)
        dashboard_list = dashboards_api.list_dashboards()
        for dashboard in dashboard_list.dashboards:
            if dashboard.title == "Saviour's Web-01 Monitoring Dashboard":
                return dashboard.id
    return None


if __name__ == '__main__':
    dashboard_id = dash_id()

    if dashboard_id is not None:
        with open("2-setup_datadog", 'w') as file:
            file.write(dashboard_id)