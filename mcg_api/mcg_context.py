#!/usr/bin/env python
# (c) Copyright 2024 Premier Heart, LLC

import json
import os
import requests
import sys
from datetime import datetime

# ----------------------------------------------------------------------
# A connection to the MCG API server using a specific token.
# This is the object used inside an McgApiConnection block.
class McgApiContext:
    def __init__(self, token, url, debug=False):
        self._token = token
        self._url = url
        self._debug = debug

    # analyze endpoint. each endpoint has its own wrapper method
    def analyze(self, request_json):
        if self._debug:
            print("sending AnalysisRequest JSON!")
        return self.send('/analyze', request_json)

    # returns a Dict containing the analysis results or an error
    def send(endpoint, request_json):
        hdr = { 'Authorization': self._token,
                'Content-Type': 'application/json' }
        resp = requests.post(url=self._url + endpoint, headers=hdr, json=data)
        if resp.status_code != 200:
            return {
                    "object-type": "http-error",
                    "timestamp": str(datetime.now),
                    "message": "Unknown error: HTTP %d" % resp.status_code
            }
        return json.loads(resp.text)

        
