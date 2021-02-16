### Solution1 Sort

`min(a, b)` will get min of a and b. So if a and b diff is large, e.g. b >> a, then b is wasted.

So what we do is make sure a and b is as close as possible. The right way to do it is sort `nums` first.

