(a)
```
s2 = 0
s3 = s0

while s3 != 0:
    s2 += s1
    s3 -= 1
```

(b) 

if you wanted to mutiply 3 by 2

s0 would = 3 

s1 would = 2

s2 starts at 0

s3 takes the value of s0 (3)

while s3 does not equal 0 it will do the loop

s2 is increased by s1 so from 0 to 2

s3 is decreased by 1 so 3 to 2

loops again

s2 is increased by s1 so from 2 to 4

s3 is decreased by 1 so 2 to 1

loops again

s2 is increased by s1 so from 4 to 6

s3 is decreased by 1 so 1 to 0

doesnt loop again because s3 = 0

s2 = 6

2 * 3 = 6

(c)
```
s0 = 10
s1 = 1

while s0 != 0:
    s2 = 0
    s3 = s0
    while s3 != 0:
        s2 += s1
        s3 -= 1
    s1 = s2
    s0 -= 1
```

(d)

The inner loop is the multiplication from b

s3 = s0 so at the start this is 10

the inner loop does the multiplication 10 * 1

after the inner loop s2 = 10

s1 then equals s2 so s1 = 10

s0 is decreased by 1 so the new value is 9

the outer loop is started again

this time s3 = 9

the inner loop does the multiplication 9 * 10

after the inner loop s2 = 90

it then proceeds to do 90 * 8 and so on until s0 = 0

by the end s1 = 3628800

(e)
