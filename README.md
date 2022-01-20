**Polynomial in Python**

Just a class for polynomial in one variable.

Supports addition, subtraction, exponential and multiplication.

Examples:
- Initializing a polynomial
  ```python
  p = Polynomial([1, 3, -4, 2])
  print(p) # x^3 + 3x^2 - 4x + 2
  ```
- Add/Subtract Polynomials
  ```python
  p1 = Polynomial([1, 2])   # x + 2
  p2 = Polynomial([3, 4])   # 3x + 4
  print(p1 + p2)            # 4x + 6
  ```
- Scalar Multiplication
  ```python
  p1 = Polynomial([2, 3])       # (2x + 3)
  p2 = -4 * p1                  # (-4)(2x +3)
  print(p2)                     # -8x - 12
  ```
- Multiplying Polynomials
  ```python
  p1 = Polynomial([2, 3])       # (2x + 3)
  p2 = Polynomial([3, 5])       # (3x + 5)
  p3 = p1 * p2                  # (2x +3)(3x + 5)
  print(p3)                     # 6x^2 + 19x + 15
  ```
- Exponentiating a polynomial
  ```python
  p = Polynomial([1, 1])       # (x + 1)
  print(p ** 2)                # x^2 + 2x + 1
  ```
- Get expression value at point
  ```python
  p = Polynomial([3, -2, 1])
  print(f"({p}) at (x = 3) is {p.value(3)}") 
  # (3x^2 - 2x + 1) at (x = 3) is 22
  ```
- Customized expression output
  ```python
  p = Polynomial([5, 3, 2], var="m")
  print(p) # 5m^2 + 3m + 2
  ```
- [Prime Generating Polynomial](Examples/PrimeGeneratingPolynomial.py) (Requires [SymPy](https://pypi.org/project/sympy/))
