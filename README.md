#Matchete

*Really dirty and hacky prototype, don't use*

Overload methods of python classes depending on the behavior of the passed arguments:

* containing an attribute
* responding to a method call
* having a type
* responding to a method call with a certain value
* having the same list structure


example:
```python
from matchete import on, Any, eq, matchable

@matchable
class A(object):
    @on('#meow')
    def a(self, cat):
        cat.meow()

    @on('#talk')
    def a(self, human):
        human.talk()

    @on(eq('.color', 'white'))
    def a(self, white):
        return True

@matchable
class Matcher(object):
    @on('#node_type', '#node_type')
    def match(self, left, right):
        code

    @on('#node_type', Any)
    def match(self, left, right):
        other_code

@matchable
class Combinator(object):
    @on([str])
    def combine(self, values):
        return ''.join(values)

    @on([int])
    def combine(self, values):
        return ' '.join(str(v) for v in values)

    @on(is_in('.value', range(0, 10)])
    def combine(self, value):
        return str(value)

```

Install
-------

`pip install matchete`
