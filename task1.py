import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def demonstrate_calculus():

    x = sp.Symbol('x')
    f_sym = x**2 + 5*sp.sin(x)
    derivative_sym = sp.diff(f_sym, x)
    
    print(f"Функция: {f_sym}")
    print(f"Производная: {derivative_sym}")


    f = lambda x: x**2 + 5*np.sin(x)
    df = lambda x: 2*x + 5*np.cos(x)
    
    cur_x = 4
    learning_rate = 0.1
    history = []

    for i in range(20):
        history.append(cur_x)
        prev_x = cur_x
        cur_x = cur_x - learning_rate * df(prev_x) 

    x_range = np.linspace(-5, 5, 100)
    plt.figure(figsize=(10, 5))
    plt.plot(x_range, f(x_range), label='Loss Function $f(x)$')
    plt.scatter(history, [f(h) for h in history], color='red', label='Optimization Steps')
    plt.title("Calculus in Action: Gradient Descent")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    demonstrate_calculus()
