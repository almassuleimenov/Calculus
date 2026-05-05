import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.calculus.util import continuous_domain, function_range

x = sp.Symbol('x', real=True)

print(--- Question 1 Composite Function ---)
f1 = x2 + 1
g1 = 3x - 2
comp_func = f1.subs(x, g1)
print(ff(g(x)) = {sp.expand(comp_func)})

print(n--- Question 2 Domain of a Function ---)
f2 = sp.sqrt(5 - x)
domain_f2 = continuous_domain(f2, x, sp.S.Reals)
print(fDomain of sqrt(5-x) {domain_f2})

print(n--- Question 3 Range of a Function ---)
f3 = x2 + 2
range_f3 = function_range(f3, x, sp.S.Reals)
print(fRange of x^2 + 2 {range_f3})

print(n--- Question 4 Piecewise Function ---)
f4 = sp.Piecewise((x2, x  0), (x + 1, x = 0))
print(ff(-2) = {f4.subs(x, -2)})
print(ff(3) = {f4.subs(x, 3)})

print(n--- Question 5 Limit of a Piecewise Function ---)
lim_left = sp.limit(f4, x, 0, dir='-')
lim_right = sp.limit(f4, x, 0, dir='+')
print(fLeft-hand limit (x-0-) {lim_left})
print(fRight-hand limit (x-0+) {lim_right})
if lim_left == lim_right
    print(The limit exists at x = 0.)
else
    print(The limit does NOT exist at x = 0 because left and right limits are different.)

# Plotting Q5
x_vals_neg = np.linspace(-3, -0.01, 100)
x_vals_pos = np.linspace(0, 3, 100)
y_vals_neg = x_vals_neg2
y_vals_pos = x_vals_pos + 1

plt.figure(figsize=(8, 4))
plt.plot(x_vals_neg, y_vals_neg, label='x^2 (x  0)', color='blue')
plt.plot(x_vals_pos, y_vals_pos, label='x + 1 (x = 0)', color='red')
plt.scatter([0, 0], [0, 1], color=['white', 'red'], edgecolor=['blue', 'red'], zorder=5) # open and closed circles
plt.title(Q5 Piecewise Function near x=0)
plt.xlabel(x)
plt.ylabel(f(x))
plt.legend()
plt.grid(True)
plt.show()

print(n--- Question 6 Radical Limit ---)
f6 = (sp.sqrt(x) - 3)  (x - 9)
print(fLimit as x-9 {sp.limit(f6, x, 9)})

print(n--- Question 7 Trigonometric Limit ---)
f7 = sp.sin(3x)  x
print(fLimit as x-0 {sp.limit(f7, x, 0)})

print(n--- Question 8 Limit at Infinity ---)
f8 = (4x2 + 1)  (2x2 - 3)
print(fLimit as x-oo {sp.limit(f8, x, sp.oo)})

print(n--- Question 9 Graph a Rational Function ---)
f9 = (x2 - 1)  (x - 1)
domain_f9 = continuous_domain(f9, x, sp.S.Reals)
print(fDomain {domain_f9})
# At x=1, the function simplifies to x+1, so the range is all Reals except 2
print(fRange Reals  {{2}} (Since there is a hole at x=1, y=2))
print(Explanation for x=1 The function is undefined (division by zero), but the limit exists and equals 2. This is a removable discontinuity (a hole).)

# Plotting Q9
x_vals9 = np.linspace(-3, 3, 400)
y_vals9 = (x_vals92 - 1)  (x_vals9 - 1)
plt.figure(figsize=(8, 4))
plt.plot(x_vals9, y_vals9, label='(x^2 - 1)(x - 1)')
plt.scatter([1], [2], color='white', edgecolor='red', zorder=5, label='Hole at x=1')
plt.title(Q9 Rational Function)
plt.xlabel(x)
plt.ylabel(f(x))
plt.legend()
plt.grid(True)
plt.show()

print(n--- Question 10 First Derivative ---)
f10 = x4 - 2x2 + x
print(fDerivative {sp.diff(f10, x)})

print(n--- Question 11 Second Derivative ---)
f11 = x3 + 3x2 - x
print(fSecond Derivative {sp.diff(f11, x, 2)})

print(n--- Question 12 Product Rule ---)
f12 = x2  sp.cos(x)
print(fDerivative {sp.diff(f12, x)})

print(n--- Question 13 Quotient Rule ---)
f13 = x  (x + 2)
print(fDerivative {sp.cancel(sp.diff(f13, x))})

print(n--- Question 14 Chain Rule ---)
f14 = sp.sin(x3)
print(fDerivative {sp.diff(f14, x)})

print(n--- Question 15 Logarithmic Derivative ---)
f15 = sp.ln(x2 + 1)
print(fDerivative {sp.diff(f15, x)})

print(n--- Question 16 Graph of a Trigonometric Function ---)
# Plotting Q16
x_vals16 = np.linspace(-2np.pi, 2np.pi, 400)
y_vals16 = np.sin(x_vals16) + np.cos(x_vals16)
plt.figure(figsize=(8, 4))
plt.plot(x_vals16, y_vals16, label='sin(x) + cos(x)', color='purple')
plt.title(Q16 Trigonometric Function)
plt.xlabel(x)
plt.ylabel(f(x))
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.grid(True)
plt.show()

print(n--- Question 17 Indefinite Integral ---)
f17 = 2x2 + 3x + 1
print(fIntegral {sp.integrate(f17, x)} + C)

print(n--- Question 18 Trigonometric Integral ---)
f18 = sp.sin(x)
print(fIntegral {sp.integrate(f18, x)} + C)

print(n--- Question 19 Exponential Integral ---)
f19 = sp.exp(3x)
print(fIntegral {sp.integrate(f19, x)} + C)

print(n--- Question 20 Definite Integral ---)
f20 = x2
print(fIntegral from 0 to 3 {sp.integrate(f20, (x, 0, 3))})

print(n--- Question 21 Area Under a Curve ---)
f21 = x2
print(fArea from 0 to 2 {sp.integrate(f21, (x, 0, 2))})

print(n--- Question 22 Improper Integral ---)
f22 = 1  x2
print(fIntegral from 1 to infinity {sp.integrate(f22, (x, 1, sp.oo))})

print("\n--- PART 2: Linear Regression & Gradient Descent ---")


hours = np.array([1, 2, 3, 4, 5, 6])
marks = np.array([40, 50, 55, 65, 70, 80])


def gradient_descent(x, y, m, b, learning_rate, epochs):
    n = len(x)
    for i in range(epochs):
        y_pred = m * x + b

        dm = (-2/n) * sum(x * (y - y_pred))
        db = (-2/n) * sum(y - y_pred)
        
        # Update weights
        m = m - learning_rate * dm
        b = b - learning_rate * db
    return m, b


m_final, b_final = gradient_descent(hours, marks, m=0, b=0, learning_rate=0.01, epochs=1000)

print(f"Optimal m: {m_final:.2f}")
print(f"Optimal b: {b_final:.2f}")


prediction = m_final * 7 + b_final
print(f"Prediction for 7 hours: {prediction:.2f}")


plt.figure(figsize=(8, 5))
plt.scatter(hours, marks, color='blue', label='Data Points')
plt.plot(hours, m_final * hours + b_final, color='red', label='Regression Line')
plt.title("Linear Regression via Gradient Descent")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
