def fractional_knapsack():
    n=int(input("Enter no of items: "))
    weights=[]
    values=[]
    for i in range(n):
        weight=float(input(f"Enter weight for item{i + 1}:  "))
        value=float(input(f"Enter value of item{i + 1}: "))
        weights.append(weight)
        values.append(value)

    capacity=float(input("Enter capacity of knapsack: "))
    res=0
    
    pairs = sorted(zip(weights, values), key = lambda x: x[1]/x[0], reverse = True)
    for pair in pairs:
        if capacity <= 0:
            break
        elif pair[0] > capacity:
            res += int(capacity * (pair[1] / pair[0]))
            capacity = 0
        elif pair[0] <= capacity:
            res += pair[1]
            capacity -= pair[0]
    print(res)

if __name__ == "__main__":
    fractional_knapsack()