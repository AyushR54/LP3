def solve_knapsack():
    n=int(input("Enter no of item: "))
    val=[]
    wt=[]
    for i in range(n):
        weight=float(input(f"Enter weight of item{i+1}: "))
        value=float(input(f"Enter value of item{i+1}: "))
        val.append(value)
        wt.append(weight)

    W=float(input(f"Enter capacity of knapsack: "))

    def knapsack(W,n):
        if n==0 or W==0:
            return 0
        if wt[n-1]>W:
            return knapsack(W,n-1)
        else:
            return max(val[n-1] + knapsack(W-wt[n-1],n-1),knapsack(W,n-1))

    print(f"The maximum value in the knapsack is: {knapsack(W,n)}")

if __name__=="__main__":
    solve_knapsack()