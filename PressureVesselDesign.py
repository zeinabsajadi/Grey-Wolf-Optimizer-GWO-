import numpy as np

def pressure_vessel(x):
    x1, x2, x3, x4 = x

    # Objective function (cost of the pressure vessel)
    cost = (0.6224*x1*x3*x4 +
            1.7781*x2*x3**2 +
            3.1661*x1**2*x4 +
            19.84*x1**2*x3)

    # Constraint equations
    g1 = -x1 + 0.0193*x3
    g2 = -x2 + 0.00954*x3
    g3 = -np.pi*x3**2*x4 - (4/3)*np.pi*x3**3 + 1296000
    g4 = x4 - 240

    # Penalty calculation for constraint violations
    penalty = 0
    for g in [g1, g2, g3, g4]:
        if g > 0:
            penalty += 1e6 * g

    # Return penalized objective value
    return cost + penalty


# -----------------------------
# Grey Wolf Optimizer (GWO)
# -----------------------------
def GWO(objf, dim, n_wolves=30, max_iter=200):

    # Lower and upper bounds of variables
    lb = np.array([0, 0, 10, 10])
    ub = np.array([100, 100, 200, 200])

    # Initialize wolf population
    wolves = np.random.uniform(lb, ub, (n_wolves, dim))

    # Initialize Alpha, Beta, and Delta wolves
    Alpha = np.zeros(dim)
    Alpha_score = float("inf")

    Beta = np.zeros(dim)
    Beta_score = float("inf")

    Delta = np.zeros(dim)
    Delta_score = float("inf")

    for t in range(max_iter):

        # Evaluate fitness of each wolf
        for i in range(n_wolves):
            fitness = objf(wolves[i])

            # Update Alpha, Beta, Delta based on fitness
            if fitness < Alpha_score:
                Alpha_score = fitness
                Alpha = wolves[i].copy()

            elif fitness < Beta_score:
                Beta_score = fitness
                Beta = wolves[i].copy()

            elif fitness < Delta_score:
                Delta_score = fitness
                Delta = wolves[i].copy()

        # Parameter 'a' decreases linearly from 2 to 0
        a = 2 - t * (2 / max_iter)

        # Update positions of wolves
        for i in range(n_wolves):
            for j in range(dim):

                A1 = 2*a*np.random.rand() - a
                C1 = 2*np.random.rand()
                D_alpha = abs(C1*Alpha[j] - wolves[i][j])
                X1 = Alpha[j] - A1*D_alpha

                A2 = 2*a*np.random.rand() - a
                C2 = 2*np.random.rand()
                D_beta = abs(C2*Beta[j] - wolves[i][j])
                X2 = Beta[j] - A2*D_beta

                A3 = 2*a*np.random.rand() - a
                C3 = 2*np.random.rand()
                D_delta = abs(C3*Delta[j] - wolves[i][j])
                X3 = Delta[j] - A3*D_delta

                # New position based on Alpha, Beta, Delta
                wolves[i][j] = (X1 + X2 + X3)/3

            # Keep wolves inside search space
            wolves[i] = np.clip(wolves[i], lb, ub)

    # Return best solution found
    return Alpha_score, Alpha


# -----------------------------
# Run the algorithm
# -----------------------------
best_score, best_solution = GWO(pressure_vessel, dim=4)

print("Best Cost:", best_score)
print("Best Solution [x1, x2, x3, x4]:", best_solution)
