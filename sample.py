import numpy as np

# حجم ثابت
V = 1000

# تابع هدف (مساحت فلز مصرفی)
def objective(r):
    h = V / (np.pi * r**2)
    area = 2 * np.pi * r**2 + 2 * np.pi * r * h
    return area


# پیاده سازی الگوریتم GWO
def gwo(num_wolves=10, max_iter=50, r_min=0.1, r_max=10):

    # تولید جمعیت اولیه گرگ ها (مقادیر تصادفی برای r)
    wolves = np.random.uniform(r_min, r_max, num_wolves)

    alpha = beta = delta = None
    alpha_score = beta_score = delta_score = float("inf")

    for iter in range(max_iter):

        # ارزیابی هر گرگ
        for i in range(num_wolves):
            fitness = objective(wolves[i])

            if fitness < alpha_score:
                delta_score = beta_score
                delta = beta

                beta_score = alpha_score
                beta = alpha

                alpha_score = fitness
                alpha = wolves[i]

            elif fitness < beta_score:
                delta_score = beta_score
                delta = wolves[i]

                beta_score = fitness

            elif fitness < delta_score:
                delta_score = fitness
                delta = wolves[i]

        # پارامتر کاهش یابنده
        a = 2 - iter * (2 / max_iter)

        # بروزرسانی موقعیت گرگ ها
        for i in range(num_wolves):

            r = wolves[i]

            r1, r2 = np.random.rand(), np.random.rand()
            A1 = 2 * a * r1 - a
            C1 = 2 * r2
            D_alpha = abs(C1 * alpha - r)
            X1 = alpha - A1 * D_alpha

            r1, r2 = np.random.rand(), np.random.rand()
            A2 = 2 * a * r1 - a
            C2 = 2 * r2
            D_beta = abs(C2 * beta - r)
            X2 = beta - A2 * D_beta

            r1, r2 = np.random.rand(), np.random.rand()
            A3 = 2 * a * r1 - a
            C3 = 2 * r2
            D_delta = abs(C3 * delta - r)
            X3 = delta - A3 * D_delta

            wolves[i] = (X1 + X2 + X3) / 3

            wolves[i] = np.clip(wolves[i], r_min, r_max)

    best_r = alpha
    best_h = V / (np.pi * best_r**2)

    return best_r, best_h, alpha_score


r, h, area = gwo()

print("Best r:", r)
print("Best h:", h)
print("Minimum area:", area)
