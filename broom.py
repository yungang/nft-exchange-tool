#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import logging
import json
import requests

BASE_URL = 'https://testnets-api.opensea.io/api/v1'


class Broom:
    def __init__(self):
        self.headers = {
            "Accept": "application/json",
            "X-API-KEY": "2f6f419a083c46de9d83ce3dbe7db601"
        }

        self.proxies = {
            'https': 'http://127.0.0.1:7890',
            'http': 'http://127.0.0.1:7890'
        }


    def retrive_assets(self):
        url = f'{BASE_URL}/assets?order_direction=desc&offset=0&limit=10'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_events(self):
        url = f'{BASE_URL}/events?only_opensea=false&offset=0&limit=20'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_collections(self):
        url = f'{BASE_URL}/collections?offset=0&limit=30'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_bundles(self):
        url = f'{BASE_URL}/bundles?limit=20&offset=0'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_single_asset(self):
        url = f'{BASE_URL}/asset/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb/1/'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_single_contract(self):
        url = f'{BASE_URL}/asset_contract/0x06012c8cf97bead5deae237070f9587f8e7a266d'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_single_collection(self):
        url = f'{BASE_URL}/collection/doodles-official'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_collection_stat(self):
        url = f'{BASE_URL}/collection/doodles-official/stats'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


    def retrive_orders(self):
        url = f'{BASE_URL}/orders?bundled=false&include_bundled=false&limit=20&offset=0&order_by=created_date&order_direction=desc&X-API-KEY=2f6f419a083c46de9d83ce3dbe7db601'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        print(resp.json())


if __name__ == '__main__':
    broom = Broom()
    # broom.retrive_assets()
    # broom.retrive_events()
    # broom.retrive_single_asset()
    # broom.retrive_collections()
    # broom.retrive_bundles()
    # broom.retrive_single_asset()
    # broom.retrive_single_contract()
    # broom.retrive_single_collection()
    # broom.retrive_collection_stat()
    broom.retrive_orders()