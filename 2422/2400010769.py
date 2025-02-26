def spiral_encrypt(R, C, s):
    # 字符到数值的映射
    char_to_num = {' ': 0}
    for i in range(26):
        char_to_num[chr(ord('A') + i)] = i + 1
    
    # 将字符串转换为数值列表
    nums = [char_to_num[char] for char in s]
    
    # 将数值转换为5位二进制字符串
    binary_str = ''.join([f'{num:05b}' for num in nums])
    
    # 计算需要补充的0的个数
    total_bits = R * C
    padding = total_bits - len(binary_str)
    binary_str += '0' * padding
    
    # 初始化矩阵
    matrix = [[-1 for _ in range(C)] for _ in range(R)]
    #-1代指没有被填充
    # 方向数组：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    row, col = 0, 0
    

    for bit in binary_str:
        matrix[row][col] = int(bit)
      
        next_row = row + directions[dir_idx][0]
        next_col = col + directions[dir_idx][1]
       
        if 0 <= next_row < R and 0 <= next_col < C and matrix[next_row][next_col] == -1:
            row, col = next_row, next_col
        else:
         
            dir_idx = (dir_idx + 1) % 4
            row += directions[dir_idx][0]
            col += directions[dir_idx][1]
    
    # 将矩阵按行连接起来
    encrypted_str = ''.join([''.join(map(str, row)) for row in matrix])
    
    return encrypted_str

# 读取输入
R, C, s = input().split(maxsplit=2)
R = int(R)
C = int(C)
s = s.strip()

# 加密并输出结果
print(spiral_encrypt(R, C, s))