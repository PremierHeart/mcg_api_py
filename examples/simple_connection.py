#!/usr/bin/env python
# (c) Copyright 2024 Premier Heart, LLC

import json
import os
import sys
from mcg_api import McgApiConnection

# ----------------------------------------------------------------------
# MAIN
# This can be used to send a request directly to the server, if the API
# token file is present in ENV['MCG_API_TOKEN_FILE']
TOKEN_PATH_KEY='MCG_API_TOKEN_FILE'
if __name__ == '__main__':
    tok = None
    if TOKEN_PATH_KEY in os.environ:
        with open(os.environ[TOKEN_PATH_KEY], 'r') as f:
            tok = f.read().strip()
    if not tok:
        sys.stderr.write("Access token file path must be in " + TOKEN_PATH_KEY + "\n")
        sys.exit(-1)

    if len(sys.argv) < 2:
        sys.stderr.write("Missing analysis_request.json argument!\n")
        sys.exit(-1)
    with open(sys.argv[1], 'r') as f:
        req = json.loads( f.read() )

    with McgApiConnection(tok) as conn:
        res = conn.analyze(req)

    print(json.dumps(res, indent=4))
