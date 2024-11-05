def simulate_tart_purchases(N, M, K):
    # 初始化每位顾客的购买总量和购买记录
    customers = [0] * N  # 每个顾客当前已购买的数量
    customer_purchases = [[] for _ in range(N)]  # 每个顾客的购买记录
    queue = list(range(N))  # 顾客队列，按顺序处理顾客
    finished_customers = []  # 完成购买的顾客列表
    current_bake = 1  # 当前烘焙的数量，从1开始
    rest_bake = 0  # 剩余未购买的数量

    # 当还有顾客在队列中时继续处理
    while queue:
        # 如果当前烘焙数量超过了最大限制K，则重置为1
        if current_bake > K:
            current_bake = 1
        
        # 取出队列中的第一个顾客的索引
        customer_index = queue.pop(0)
        
        # 计算该顾客此次购买的数量，不能超过他们的购买上限M，且不能超过当前可购买的数量
        purchase_amount = min(current_bake + rest_bake, M - customers[customer_index])
        
        # 更新该顾客的总购买量
        customers[customer_index] += purchase_amount
        
        # 记录该顾客的购买情况
        customer_purchases[customer_index].append(purchase_amount)
        
        # 如果该顾客还没有达到购买上限M，则将其重新放入队列中
        if customers[customer_index] < M:
            queue.append(customer_index)
        else:
            # 否则，将该顾客添加到完成购买的列表中
            finished_customers.append(customer_index + 1)  # +1是因为顾客编号是从1开始的
            
        # 更新剩余的烘焙数量
        if current_bake - purchase_amount > 0:
            # 如果当前烘焙数量大于购买数量，增加剩余烘焙数量
            rest_bake += current_bake - purchase_amount
        else:
            # 否则，减少剩余烘焙数量
            rest_bake -= purchase_amount - current_bake
        
        # 当前烘焙数量自增1，以便下一个顾客
        current_bake += 1

    # 打印每位顾客的购买情况
    print("顾客的购买情况：")
    for i, purchases in enumerate(customer_purchases):
        print(f"顾客{i + 1}\t购买次数及数量: {purchases}")
    
    # 打印完成购买的顾客顺序
    print("完成购买的顾客顺序：", finished_customers)

# 获取用户输入并调用函数
N = int(input("顾客数量："))  # 输入顾客数量
M = int(input("总购买数："))   # 输入每位顾客的购买上限
K = int(input("烘培上限："))    # 输入当前烘焙数量的最大限制
simulate_tart_purchases(N, M, K)
