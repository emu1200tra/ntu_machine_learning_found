import time
import numpy as np


def ridge_reg(x, y, lmd):
    z = np.linalg.inv(np.dot(x.transpose(), x) + lmd * np.eye(x.shape[1]))
    return np.dot(np.dot(z, x.transpose()), y)


def err_01(x, y, w):
    return np.sign(np.dot(x, w)) != y


def err_func(x, y, w, n):
    e = 0.0
    for i in range(n):
        if err_01(x[i], y[i], w):
            e += 1.0
    return e / n


def read_file(f):
    x_d = []
    y_d = []
    with open(f, 'r') as d:
        for line in d:
            l = line.split()
            x = [1.0] + [float(v) for v in l[: -1]]
            x_d.append(x)
            y_d.append(int(l[-1]))
    return np.array(x_d), np.array(y_d), len(y_d)


def quiz13(lmd=10):
    x_in, y_in, n_in = read_file("train.txt")
    x_out, y_out, n_out = read_file("test.txt")
    w_reg = np.array(ridge_reg(x_in, y_in, lmd)).flatten()
    print w_reg
    e_in = err_func(x_in, y_in, w_reg, n_in)
    e_out = err_func(x_out, y_out, w_reg, n_out)
    return e_in, e_out




def main():
    np.random.seed()
    start_time = time.time()
    print("q13: \n", quiz13())
    # print("q14: \n", quiz14())
    # print("q15: \n", quiz15())
    # print("q16: \n", quiz16())
    # print("q17: \n", quiz17())
    # print("q18: \n", quiz18())
    # print("q19: \n", quiz1920())
    print("Taken total %f seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()