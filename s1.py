
from multiprocessing.dummy import Pool

import requests

pool = Pool(20) # Creates a pool with ten threads; more threads = more concurrency.
                # "pool" is a module attribute; you can be sure there will only
                # be one of them in your application
                # as modules are cached after initialization.

if __name__ == '__main__':
    futures = []
    for x in range(10000):
        futures.append(pool.apply_async(requests.get, ['https://siberdeyiz.com/u/onecame33/9394']))
    # futures is now a list of 10 futures.
    for future in futures:
        print(future.get())
