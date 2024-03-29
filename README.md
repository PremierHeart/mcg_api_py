Simple wrapper for MCG Stateless API server.

Example:
```python
    with open(sys.argv[1], 'r') as f:
        req = json.loads( f.read() )
    with McgApiConnection(tok) as conn:
        res = conn.analyze(req)
    print(json.dumps(res, indent=4)) 
```
