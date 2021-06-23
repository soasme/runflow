---
sidebar: auto
---

# Handle DateTime Objects

## Built-in Function `datetime`

You can provide a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects) object by using `datetime()` function:

```
attrib = datetime(2020, 1, 1, 0, 0, 0)
```

This function currently only creates a Naive datetime object, e.g. no tzinfo associated.

## Built-in Function `todatetime`

You can provide a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects) object by using `todatetime()` function:

```python
attrib = todatetime("2020-01-01T00:00:00Z")
```
