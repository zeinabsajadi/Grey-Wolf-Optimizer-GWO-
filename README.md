# Grey Wolf Optimizer (GWO)

This repository contains an implementation of the **Grey Wolf Optimizer (GWO)** algorithm along with several example optimization problems.  
GWO is a nature‑inspired metaheuristic that models the leadership hierarchy and cooperative hunting strategy of grey wolves to solve continuous optimization tasks.

---

## 🐺 What is GWO?

The **Grey Wolf Optimizer**, introduced by Mirjalili et al. (2014), is inspired by the natural behavior of grey wolves. It incorporates:

### • Wolf Hierarchy
- **Alpha (α)** – Leaders  
- **Beta (β)** – Second level  
- **Delta (δ)** – Third level  
- **Omega (ω)** – Followers  

### • Main Behavioral Mechanisms
- **Encircling the prey**  
- **Hunting with leaders (α, β, δ)**  
- **Attacking the prey / convergence**

These behaviors are modeled mathematically to guide the wolves toward the global optimum of a given objective function.

### • Common Parameters
- `n_wolves`: number of search agents  
- `max_iter`: maximum number of iterations  
- `dim`: dimensionality of the search space  
- `lb`, `ub`: variable bounds (lower and upper limits)

---

## 📂 Repository Structure



---

## 🎯 Applications

GWO can be applied to a wide range of optimization tasks, including:

- Engineering design optimization  
- Mathematical benchmark functions  
- Black‑box optimization problems  
- Hyperparameter tuning  
- Feature selection  
- General metaheuristic‑based problem solving  

This repository can serve as a starting point for such applications.

---

## 📚 Reference

If you use this implementation in academic work, cite the original GWO paper:

Mirjalili, S., Mirjalili, S. M., & Lewis, A. (2014).  
*Grey Wolf Optimizer.* **Advances in Engineering Software**, 69, 46–61.
