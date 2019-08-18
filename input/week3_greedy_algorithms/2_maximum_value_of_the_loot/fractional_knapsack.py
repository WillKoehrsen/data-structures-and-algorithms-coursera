# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    unit_values = [v/w for w, v in zip(weights, values)]
    tup_values = [(u, w, v) for u, w, v in zip(unit_values, weights, values)]
    total_weight = 0
    while total_weight < capacity:
        if not tup_values:
            break
        available_weight = capacity - total_weight
        max_unit_value, max_weight, max_value = max(tup_values)
        if max_weight <= available_weight:
            total_weight += max_weight
            value += max_value
        else:
            total_weight += available_weight
            value += max_unit_value * available_weight
        tup_values.remove((max_unit_value, max_weight, max_value))
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
