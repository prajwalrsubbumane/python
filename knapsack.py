def knapsack_max_profit(weights,costs,capacity):
    num_items=len(weights)
    table=[[0]*(capacity+1) for _ in range(num_items+1)]
    for i in range(1,num_items+1):
        for j in range(1,capacity+1):
            if weights[i-1]<=j:
                table[i][j]=max(costs[i-1]+table[i-1][j-weights[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    selected_items=[]
    total_weight=capacity
    for i in range(num_items,0,-1):
        if table[i][total_weight]!=table[i-1][total_weight]:
            selected_items.append(i-1)
            total_weight-=weights[i-1]
    return table[num_items][capacity],selected_items
weights=[]
costs=[]
n=int(input("Enter the no of types of coffee: "))
for i in range(n):
    w=int(input(f"Weight of coffee {i}: "))
    c=int(input(f"Cost of coffee {i}: "))
    costs.append(c)
    weights.append(w)
capacity=int(input("Enter the capacity: "))
max_profit,selected_items=knapsack_max_profit(weights,costs,capacity)
print("Maximum Profit: ",max_profit)
print("Selected coffee beans (index): ",selected_items)
print("Selected coffee beans (weight): ",[weights[i] for i in selected_items])
print("Selected coffee beans (cost): ",[costs[i] for i in selected_items])

# Enter the no of types of coffee: 4
# Weight of coffee 0: 2
# Cost of coffee 0: 10
# Weight of coffee 1: 3
# Cost of coffee 1: 20
# Weight of coffee 2: 4
# Cost of coffee 2: 30
# Weight of coffee 3: 5
# Cost of coffee 3: 40
# Enter the capacity: 10
# Maximum Profit:  70
# Selected coffee beans (index):  [3, 1, 0]
# Selected coffee beans (weight):  [5, 3, 2]
# Selected coffee beans (cost):  [40, 20, 10]
