import random
import time
import tabulate



def qsort_first_pivot(a):
    """
    Quicksort implementation with the first element as the pivot.
    """
    if len(a) <= 1:
       return a
    else:
        pivot = a[0]
        left = [x for x in a[1:] if x <= pivot]
        right = [x for x in a[1:] if x > pivot]
        return qsort_first_pivot(left) + [pivot] + qsort_first_pivot(right)


def qsort_random_pivot(a):
    """
    Quicksort implementation with a random element as the pivot.
    """
    if len(a) <= 1:
        return a
    else:
        pivot_index = random.randint(0, len(a) - 1)
        pivot = a[pivot_index]
        left = [x for i, x in enumerate(a) if i != pivot_index and x <= pivot]
        right = [x for i, x in enumerate(a) if i != pivot_index and x > pivot]
        return qsort_random_pivot(left) + [pivot] + qsort_random_pivot(right)

def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
  """
  Compare the running time of different sorting algorithms.

  Returns:
    A list of tuples of the form
    (n, qsort-first-pivot-time, qsort-random-pivot-time)
    indicating the number of milliseconds it takes
    for each method to run on each value of n
  """
  result = []
  for size in sizes:
      # create list in ascending order
      mylist = list(range(size))
      # shuffles list if needed
      random.shuffle(mylist)

      result.append([
          len(mylist),
          time_search(qsort_first_pivot, mylist),
          time_search(qsort_random_pivot, mylist),
          time_search(sorted, mylist)
      ])
  return result
def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-first-pivot', 'qsort-random-pivot', 'timsort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()