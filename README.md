## channel in python demo

> In order to use channel in python which can be used in golang frequently.

### Usage

```
from main import MyChannel

ch = MyChannel()
// ch.callback = func or not
ch.ch = 'sth' // ch <- 'sth'
s = ch.ch // s <- ch
while s:
    callback(s)
    s = ch.ch
```