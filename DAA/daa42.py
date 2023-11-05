class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_bb(items, capacity):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0

    def bound(node, n, weight, value):
        if weight > capacity:
            return 0

        bound_value = value

        for i in range(node, n):
            if weight + items[i].weight <= capacity:
                weight += items[i].weight
                bound_value += items[i].value
            else:
                bound_value += (capacity - weight) * (items[i].value / items[i].weight)
                break

        return bound_value

    def knapsack(node, weight, value):
        nonlocal max_value

        if weight <= capacity and value > max_value:
            max_value = value

        if bound(node, len(items), weight, value) > max_value:
            knapsack(node + 1, weight + items[node].weight, value + items[node].value)

        if bound(node, len(items), weight, value) > max_value:
            knapsack(node + 1, weight, value)

    knapsack(0, 0, 0)
    return max_value

if __name__ == "__main__":
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    capacity = 50
    max_value = knapsack_bb(items, capacity)
    print(f"Maximum value in the knapsack: {max_value}")