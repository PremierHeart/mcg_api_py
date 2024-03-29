#!/usr/bin/env python
# (c) Copyright 2024 Premier Heart, LLC

import json
import os
import requests
import sys
from datetime import datetime



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

