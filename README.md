#Matchete

example:
```python
from matchete import on, Any, eq

class A(self):
    @on('#meow')
    def a(self, cat):
        cat.meow()

    @on('#talk')
    def a(self, human):
        human.talk()

    @on(eq('.color', 'white'))
    def a(self, white):
        return True

class Matcher(self):
    @on('#node_type', '#node_type')
    def match(self, left, right):
        code
    
    @on('#node_type', Any)
    def match(self, left, right):
        other_code
```
