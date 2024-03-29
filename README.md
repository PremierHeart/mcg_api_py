# mcg_api
Simple wrapper for MCG Stateless API server.

##Example:
```python
    from mcg_api import McgApiConnection
    with open(sys.argv[1], 'r') as f:
        req = json.loads( f.read() )
    with McgApiConnection(tok) as conn:
        res = conn.analyze(req)
    print(json.dumps(res, indent=4)) 
```
## License
(c) Copyright 2024 Premier Heart, LLC
Released for public use under the Apache 2.0 License.
