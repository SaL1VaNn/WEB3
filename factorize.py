from multiprocessing import Pool

def factorize(number):
    
    results = {}
    results[number] = set()
    for i in range(1,  number +1):
            if number % i == 0:
                results[number].add(i)
    
    print ( list(set.intersection(*[value for value in results.values()])))

if __name__ == '__main__':
    a = [128, 255, 99999, 10651060]

    with Pool(processes=4) as pool:
         pool.map(factorize,a)