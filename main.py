import numpy as np
        
def F(x, y):
    f1 = np.sin(x) + 2*y - 2
    f2 = 3*x + np.cos(y-1) - 0.7
    return np.array([f1,f2])

def W(x, y):
    return np.array([
        [np.cos(x), 2],
        [3, -np.sin(y-1)]
    ])

def W_inv(x: float, y: float):
    return 1/det_W(x, y) * np.array([
        [-np.sin(y), -2],
        [-3, np.cos(x)]
    ])

def det_W(x, y):
    return -np.sin(y - 1)*np.cos(x) - 6

def main():
    x0, y0 = 0, 0
    xi, yi = x0, y0
    all_aproximations = []
    all_aproximations.append(np.array([np.inf, np.inf]))
    for i in range(1, 10000):
        Xi = np.array([xi, yi]) - np.dot(W_inv(xi, yi), F(xi, yi))
        all_aproximations.append(Xi)
        xi, yi = Xi[0], Xi[1]
        if np.linalg.norm(Xi-all_aproximations[i-1]) < 1e-9:
            print(f"Решение сошлось к {Xi} на {i} итерации c начальным вектором X0({x0}, {y0})")
            break
        print(Xi)



if __name__ == "__main__":
    main()