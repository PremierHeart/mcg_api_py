#!/usr/bin/env python
# (c) Copyright 2024 Premier Heart, LLC

import json
import os
import requests
import sys
from datetime import datetime

# ----------------------------------------------------------------------
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

        

# ----------------------------------------------------------------------
class McgApiConnection:
    DefaultUrl='httpa://api.premierheart.com/api/v1'
    def __init__(self, token, url=DefaultUrl, debug=False):
        self._ctx = McgApiContext(token, url, debug)
        self._debug = debug

    def __enter__(self):
        if self._debug:
            print("Connecting to API Server")
        return self.ctx

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self._debug:
            print("Disconnecting from API Server")
        # API is stateless: No need to disconnect
        pass

# ----------------------------------------------------------------------
# MAIN
# This can be used to osend a request directly to the server, if the API
# token file is present in ENV['MCG_API_TOKEN_FILE']
if __name__ == '__main__':
    tok = None
    if 'MCG_API_TOKEN_FILE' in os.environ:
        with open(os.environ[TOKEN_PATH_KEY], 'r') as f:
            tok = f.read().strip()
    if not tok:
        sys.stderr.print("Access token file path must be in MCG_API_TOKEN_FILE")
        return -1

    if len(sys.argv) < 1:
        sys.stderr.print("Missing analysis_reques.json argument!")
        return -1
    with open(sys.argv[1], 'r') as f:
        req = json.loads( f.read() )

    #with McgApiConnection(token) as conn:
    with McgApiConnection(token, "http://localhost:8080/api/v1") as conn:
        res = conn.analyze(req)

    print(json.dumps(res, indent=4))
