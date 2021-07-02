---
sidebar: auto
---

# Built-In Functions

## `datetime()`

`datetime()` takes year, month, day, hour, minute, second, microsecond to construct a
[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects).

Examples:

```
> datetime(2020, 1, 1)
datetime(2020, 1, 1, 0, 0, 0)

> datetime(2020, 1, 1, 0, 0, 0)
datetime(2020, 1, 1, 0, 0, 0)
```

Note this function creates a Naive datetime object.

## `todatetime()`

`todatetime()` takes a string to construct a
[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects).

Examples:

```
> todatetime("2020-01-01T00:00:00Z")
datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
```

## `call()`

`call()` takes four parameters.

1. The object.
2. The method name of object.
3. The list of arguments (optional).
4. The keyword of arguments (optional).

Examples:

```
> call("xyz", "upper")
"XYZ"

> call("xyz.abc", "replace", ["abc", "ABC"], {})
"XYZ.ABC"
```

## `tojson()`

`tojson()` takes one parameter and formats it in JSON.

Examples:

```
> tojson({ key = "value" })
"{\"key\": \"value\"}"
```

`tojson()` supports more controlling parameters using `...` syntax.

Examples:

Set indentation `indent`:

```
> tojson({ key = "value" }, { indent = 2 }...)
"{\n  \"key\": \"value\"\n}"
```

Set separators `separators`:

```
> tojson([1,2,3], {separators=[",  ", ":  "]}...)
"[1,  2,  3]"
```

Sort keys `sort_keys`:

```
> tojson({ "k2": 2, "k1": 1 }, { sort_keys = true }...)
"{\"k1\": 1, \"k2\": 2}"
```


## `concat()`

`concat()` concats multiple lists.

Examples:

```
> concat(["echo"], ["hello", "world"])
["echo", "hello", "world"]
```

## `join()`

`join()` joins multiple strings by a separator.

Examples:

```
> join(" ", ["echo", "hello", "world"])
"echo hello world"
```
