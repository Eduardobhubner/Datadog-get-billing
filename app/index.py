import requests
import os
import datetime


def get_time():

    # Get the current date
    current_date = datetime.datetime.now()
    current_month_formatted = current_date.strftime('%Y-%m')
    return current_month_formatted

def generate_syout_billing():

    date_now = get_time()

    # Environment variables
    api_key = os.environ.get("API_KEY")
    dd_key = os.environ.get("DD_KEY")
    url = os.environ.get("URL_KEY", "https://api.datadoghq.com/api/v1/usage/billable-summary")
    date = os.environ.get("DATA_KEY", date_now) 

    date_format = "?month={}".format(date)

    headers = {"DD-API-KEY": api_key, "DD-APPLICATION-KEY": dd_key}
    response = requests.get(url + date_format, headers=headers)

    if response.status_code == 200:

        dataframe = response.json()
        usage_billing = dataframe["usage"]

        # Criando lista de objetos contendo sub_org e consumo de licenças
        for usage in usage_billing:
            org_name = usage["org_name"]

            for key, value in usage["usage"].items():
                usage = value["org_billable_usage"]
                type_usage = value["usage_unit"]
                syout = f"{org_name}, {key}, {usage}, {type_usage}"
                print(syout)

    else:

        print("Error:", response.status_code)


generate_syout_billing()
