import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_karlo(num_trials):
    res = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_trials):
        r = roll_dice()
        res[r] += 1
    
    probabilities = {key: value / num_trials * 100 for key, value in res.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for key, value in probabilities.items():
        print(f"{key}\t{value:.2f}% ({value/100:.2f})")

def main():
    num = 1000000
    probabilities = monte_karlo(num)
    print_probabilities(probabilities)

if __name__ == "__main__":
    main()
