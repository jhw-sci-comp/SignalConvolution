from math import pow

def calculateTrapezoidalRule(func_arg, interval_arg, step_size_arg):
    a = min(interval_arg)
    b = max(interval_arg)
    n_steps = int((b - a)/step_size_arg)
    sum_temp = 0
    t = a

    for i in range(1, n_steps):
        t = round(t + step_size_arg, 10)
        sum_temp += func_arg(t)

    return round(step_size_arg * ((func_arg(a) + func_arg(b)) / 2 + sum_temp), 10)

def calculateRombergExtrapolation(func_arg, interval_arg):
    a = min(interval_arg)
    b = max(interval_arg)
    n_steps = 10
    val_trapezoidal_prev = []
    val_trapezoidal_next = []
    step_size_i = 0.0

    for i in range(0, n_steps + 1):
        step_size_i = (b - a)/pow(2, i)
        val_trapezoidal_prev.append(calculateTrapezoidalRule(func_arg, interval_arg, step_size_i))

    for k in range(1, n_steps + 1):
        for i in range(0, n_steps - k + 1):
            val_temp = val_trapezoidal_prev[i+1] + (val_trapezoidal_prev[i+1] - val_trapezoidal_prev[i])/(pow(4, k) - 1)
            val_trapezoidal_next.append(val_temp)
        val_trapezoidal_prev = val_trapezoidal_next.copy()
        val_trapezoidal_next.clear()

    return val_trapezoidal_prev[0]