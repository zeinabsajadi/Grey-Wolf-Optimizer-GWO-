# Grey Wolf Optimizer (GWO)

This repository contains an implementation of the **Grey Wolf Optimizer (GWO)** algorithm along with several example optimization problems.  
GWO is a nature-inspired metaheuristic that simulates the leadership hierarchy and hunting strategy of grey wolves to solve continuous optimization problems.

---

## 🐺 What is GWO?

The **Grey Wolf Optimizer**, introduced by Mirjalili et al. (2014), is based on:

- A hierarchical structure of wolves:
  - **Alpha (α)** – leader
  - **Beta (β)** – second level
  - **Delta (δ)** – third level
  - **Omega (ω)** – followers
- Three main behaviors:
  - **Encircling the prey**
  - **Hunting**
  - **Attacking / converging to the prey**
 
  - Common GWO parameters (check your code to confirm):

    n_wolves: number of search agents (population size)  
    max_iter: maximum number of iterations
    dim: dimension of the search space
    lb, ub: lower and upper bounds of variables

These behaviors are modeled mathematically to search for the global optimum of a given objective function.

---

## 📂 Repository Structure

---
## 🎯 Applications
-GWO can be applied to:

  -Engineering design optimization
  -Mathematical benchmark functions
  -Black-box optimization problems
  -Hyperparameter tuning
  -Feature selection and other metaheuristic-based tasks
  -This repository can be used as a starting point for such applications.
---
  ##📚 Reference
-If you use this implementation in your academic work, you may refer to the original GWO paper:

 -Mirjalili, S., Mirjalili, S. M., & Lewis, A. (2014).



