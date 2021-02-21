### Solution1 DP

- replace: ends with n and must replaced one
- nonreplace: ends with n and must not replaced

for replace, there are three cases:

- `n * n`: replace current n, and start this as new subarray.
- `n * n + nonreplace`: replace current n and plus former nonreplace subarray.
- `n + replace`: already replaced before and add current n to subarray.

for nonreplace, there are only two cases:

- `n`: n start as a new subarray.
- `n + nonreplace`: n plus former nonreplace subarray.

