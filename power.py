import numpy as np # type: ignore

def power(arr, base, epsilon):
    a = base / np.linalg.norm(base)
    b = np.dot(arr, a)
    b = b / np.linalg.norm(b)

    while max(abs(a - b)) > epsilon:
        a = b
        b = np.dot(arr, b)
        b = b / np.linalg.norm(b)
    
    return b

def shmidt(vec, vecs):

    for i in range(len(vecs)):
        vec -= (np.dot(vec, vecs[i]) / np.dot(vecs[i], vecs[i])) * vecs[i]

    return vec / np.linalg.norm(vec)

def power_method(arr, base, epsilon):
    vecs = []
    n = arr.shape[0]

    vecs.append(power(arr, base, epsilon))

    for i in range(1, n):
        new_base = np.random.rand(n)
        new_base = shmidt(new_base, vecs)
        vecs.append(power(arr, new_base, epsilon))

    return vecs

def main():
    arr = np.array([[6.0, 0.0, 0.0], [0.0, 3.0, 1.0], [0.0, 1.0, 3.0]])
    base = np.random.rand(3)
    epsilon = 1e-8

    print(power_method(arr, base, epsilon))

if __name__ == "__main__":
    main()