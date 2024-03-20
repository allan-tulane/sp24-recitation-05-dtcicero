# CMPS 2200 Reciation 5
## Answers

**Name:** Daniel Cicero


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

Comparison  of first-pivot and random-pivot with randomly shuffled input n: 

|      n |   qsort-first-pivot |   qsort-random-pivot |
|--------|---------------------|----------------------|
|    100 |               0.188 |                0.369 |
|    200 |               0.417 |                0.708 |
|    500 |               1.073 |                2.834 |
|   1000 |               2.588 |                4.246 |
|   2000 |               5.102 |                9.035 |
|   5000 |              62.298 |               27.137 |
|  10000 |              82.506 |              187.854 |
|  20000 |             212.923 |              297.844 |
|  50000 |             609.019 |              818.792 |
| 100000 |            1134.238 |             2063.143 |

Comparison of first-pivot and random-pivot with pre-sorted input n: 

When I pre-sorted the input instead of randomizing it, both techniques of qsort routinely encountered the recursion error: "RecursionError: maximum recursion depth exceeded in comparison". This is due to the property of quicksort to have a much higher work (up to O(n^2) for sorted or nearly sorted lists). This is because in a sorted list, it is much harder for qsort to pick an effective pivot, (in case of qsort-first-pivot picking the first and smallest value of a sorted list) leading to an excess of recursive calls, the degredation of the effectiveness of the algorithm, and a maximum recursion depth error.


- **1c.**

|      n |   qsort-first-pivot |   qsort-random-pivot |   timsort |
|--------|---------------------|----------------------|-----------|
|    100 |               0.182 |                0.300 |     0.013 |
|    200 |               0.368 |                0.631 |     0.021 |
|    500 |               0.981 |                2.054 |     0.081 |
|   1000 |              20.061 |                3.963 |     0.127 |
|   2000 |               5.358 |               48.083 |     0.317 |
|   5000 |              36.210 |               64.091 |     0.753 |
|  10000 |              41.497 |              156.163 |     2.349 |
|  20000 |             238.920 |              410.931 |     4.101 |
|  50000 |             431.108 |              752.478 |    17.377 |
| 100000 |            1099.213 |             1996.416 |    93.876 |