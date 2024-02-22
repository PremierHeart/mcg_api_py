#!/usr/bin/env python
# (c) Copyright 2024 Premier Heart, LLC

import json
import os
import sys
from mcg_api import McgApiConnection

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
