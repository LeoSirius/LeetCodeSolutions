### Solution1 Hash

Use a hash table `counter` to count original nums' frequency, and find degree.

Then find the max degree's correspoding number, then find's left-most and right-most index.

To do that, use two dict `left` and `right` to store every number left and right-most index.

