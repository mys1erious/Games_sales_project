import sys

import requests
import json


URL = "http://localhost:8000/api/v1/sales/"
FILE_PATH = 'data_sample_processed.json'
EMAIL = 'admin@gmail.com'
PASSWORD = 'admin'


def sales_get_request(url, **kwargs):
    if 'page_size' in kwargs:
        url+=f'?page_size={kwargs["page_size"]}'
    r_get = requests.get(
        url=url,
        auth=(EMAIL, PASSWORD)
    )
    return r_get.json()


def sales_post_request(data):
    r_post = requests.post(
        url=URL,
        data=json.dumps(data, indent=2),
        auth=(EMAIL, PASSWORD),
        headers={
            'Content-Type': 'application/json',
        }
    )
    return r_post


def sales_delete_request(uuid):
    url = f'{URL}{uuid}/'
    r_del = requests.delete(
        url=url,
        auth=(EMAIL, PASSWORD),
        headers={
            'Content-Type': 'application/json',
        }
    )
    return r_del


def delete_sales(uuids):
    for uuid in uuids:
        response = sales_delete_request(uuid)
        print(response)


def post_sales():
    with open(FILE_PATH, 'r') as f:
        data = json.load(f)
        samples = data['samples']

        for i in range(9382, len(samples)):
            r = sales_post_request(samples[i])
            if not r.ok:
                print(i, r.status_code, r.json())


def get_all_sales(url):
    return sales_get_request(URL, page_size=sys.maxsize)


def get_all_sales_uuids():
    sales = get_all_sales(URL)
    sales_list = sales['sales']

    uuids = []
    for sale in sales_list:
        uuids.append(sale['uuid'])

    return uuids


if __name__ == '__main__':
    ...
    post_sales()

    # uuids = get_all_sales_uuids()
    # print(uuids)
    # delete_sales(uuids)
