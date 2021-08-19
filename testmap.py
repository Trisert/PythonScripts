import multiprocessing

def mul(x):
    return x*x

if __name__ == '__main__':
    with multiprocessing.Pool(8) as p:
        print(p.map(mul, range(123456789)))
