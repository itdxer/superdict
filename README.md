# SuperDict

SuperDict - it's like dict, but better.

You don't change you dictionary to something new, you just make it better.

Module contains only 13 rows of code and valid by PEP8.


```python
>>> from superdict import SuperDict
>>>
>>> data = SuperDict()
>>>
>>> data.so.how.it = 'works'
>>> data
{'so': {'how': {'it': 'works'}}}
>>> data.so
{'how': {'it': 'works'}}
>>>
>>> data.test.me.please = 42
>>> data
{'test': {'me': {'please': 42}}, 'so': {'how': {'it': 'works'}}}
>>>
>>> del data.test.me
>>> data
{'test': {}, 'so': {'how': {'it': 'works'}}}
>>>
>>> data['so']['how']
{'it': 'works'}
>>>
>>> default_data = SuperDict({'default': {'x': 'y'}})
>>> default_data
{'default': {'x': 'y'}}
>>> default_data.default.x
'y'
>>>
>>> default_data = SuperDict({'default': SuperDict({'x': 'y'})})
>>> default_data
{'default': {'x': 'y'}}
>>> default_data.default.x
'y'
```

In another cases this class works like a dict.

```python
>>> default_data['unknown-key']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'unknown-key'
>>>
>>> default_data['set'] = 'correct'
>>> default_data['new-set']['value'] = 'wrong'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'new-set'
```
