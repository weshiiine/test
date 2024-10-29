def simulate_tart_purchases(N, M, K):
    customers = [0] * N
    customer_purchases = [[] for _ in range(N)]
    queue = list(range(N))
    finished_customers = []
    current_bake = 1
    rest_bake=0
    while queue:
        if current_bake > K:
            current_bake = 1
        
        customer_index = queue.pop(0)
        purchase_amount = min(current_bake+rest_bake, M - customers[customer_index])
        customers[customer_index] += purchase_amount
        customer_purchases[customer_index].append(purchase_amount)
        if customers[customer_index] < M:
            queue.append(customer_index)
        else:
            finished_customers.append(customer_index + 1)
        if current_bake-purchase_amount>0:
            rest_bake+=current_bake-purchase_amount
        else:
            rest_bake-=purchase_amount-current_bake
        current_bake += 1

    print("顾客的购买情况：")
    for i, purchases in enumerate(customer_purchases):
        print(f"顾客{i+1}\t购买次数及数量: {purchases}")
    
    print("完成购买的顾客顺序：", finished_customers)

N=int(input("顾客数量："))
M=int(input("限购数量："))
K=int(input("最多烘培："))
simulate_tart_purchases(N, M, K)