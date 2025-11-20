import numpy as np

def shmidt(vec, vecs):

    for i in range(len(vecs)):
        vec -= (np.dot(vec, vecs[i]) / np.dot(vecs[i], vecs[i])) * vecs[i]

    return vec / np.linalg.norm(vec)

def cgs_qr(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    vecs = []

    for i in range(n):
        ai = A[:, i].copy()

        for j in range(i):
            R[j, i] = np.dot(vecs[j], ai)
            ai = ai - R[j, i] * vecs[j]

        qi = shmidt(ai, vecs)

        R[i, i] = np.linalg.norm(ai)

        Q[:, i] = qi
        vecs.append(qi)

    return Q, R

def main():
    A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
    Q, R = cgs_qr(A)
    print(Q)
    print(R) 

    return 

if __name__ == "__main__":
    main()