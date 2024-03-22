def greedy_algorithm(items, budget):
    item_list = [(name, data["cost"], data["calories"], data["calories"]/data["cost"]) for name, data in items.items()]
    sorted_items = sorted(item_list, key=lambda x: x[3], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item in sorted_items:
        if total_cost + item[1] <= budget:
            total_cost += item[1]
            total_calories += item[2]
            chosen_items.append(item[0])

    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if items[i - 1]["cost"] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1]["calories"] + dp[i - 1][j - items[i - 1]["cost"]])
            else:
                dp[i][j] = dp[i - 1][j]

    total_calories = dp[n][budget]
    total_cost = budget
    chosen_items = []


    for i in range(n, 0, -1):
        if total_calories <= 0:
            break
        if total_calories == dp[i - 1][total_cost]:
            continue
        else:
            chosen_items.append(list(items.keys())[i - 1])
            total_calories -= items[list(items.keys())[i - 1]]["calories"]
            total_cost -= items[list(items.keys())[i - 1]]["cost"]

    return chosen_items, budget - total_cost, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Chosen items:", greedy_result[0])
print("Total cost:", greedy_result[1])
print("Total calories:", greedy_result[2])

print("\nDynamic Programming:")
print("Chosen items:", dp_result[0])
print("Total cost:", dp_result[1])
print("Total calories:", dp_result[2])
