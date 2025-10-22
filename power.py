import numpy as np

def power(arr, base, epsilon):
    a = base
    b = np.dot(arr, base)
    b = b / max(b)

    while max(abs(a - b)) > epsilon:
        a = b
        b = np.dot(arr, b)
        b = b / max(b)
    
    return b

def main():
    arr = np.array([[2, 1], [2, 3]])
    base = np.array([[1], [1]])
    epsilon = 0.001
    print(power(arr, base, epsilon))

if __name__ == "__main__":
    main()