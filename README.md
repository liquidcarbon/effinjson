# Effin JSON
A script for calling Python functions from a JSON file (fn'ing, or effin a JSON).  Specific Python methods set in a JSON file are called using `getattr` to safely `exec`(execute) /`eval`(evaluate) external commands.

## Key business logic
```
j = json.load(file)
...
for k, v in j.items():
    if hasattr(fnClass, v['fn']):
        result = getattr(fnClass, v['fn'])(v['args'])
    else:
        result = 'function "%s" not defined' % v['fn']
```
## Examples
```
$ python3 fj.py good.json
sum([2, 3, 5, 10]) = 20
divide([1001, 13]) = 77.0
cleanstring(   The quick lazy dogs 	jump over purple    fox     	) = The quick lazy dogs jump over purple fox
isprime(1000000007) = True
do_whatever(42) = function "do_whatever" not defined

$ python3 fj.py bad.json
sum([2, 3, 5, 'ten']) = arguments must be numeric
divide([1001, 0]) = are you dividing by zero?
cleanstring(123) = argument must be a string
isprime(0) = None
do_whatever() = function "do_whatever" not defined

 {
    "sum": {
        "fn": "sum",
        "args": [
            2,
            3,
            5,
            "ten"
        ],
        "result": "arguments must be numeric"
    },
    "foo": {
        "fn": "divide",
        "args": [
            1001,
            0
        ],
        "result": "are you dividing by zero?"
    },
    "remove_extra_spaces": {
        "fn": "cleanstring",
        "args": 123,
        "result": "argument must be a string"
    },
    "is_prime_number": {
        "fn": "isprime",
        "args": 0,
        "result": null
    },
    "qwerty": {
        "fn": "do_whatever",
        "args": "",
        "result": "function \"do_whatever\" not defined"
    }
}

```
