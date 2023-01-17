def compute_operations(n):

    NumOps = []
    Ops = []
    OpSum = []

    for m in range(n + 1):
        NumOps.append(float('inf'))
        Ops.append(0) # 0 means no ops; 1 means +1; 2 means *2; 3 means *3

    NumOps[0] = 0  # represents the min num taken

    for CurNum in range(1, n + 1):
        if (CurNum%3 == 0):
            CurOp = NumOps[int((CurNum)/3)] + 1
            if (NumOps[CurNum] > CurOp):
                NumOps[CurNum] = CurOp
                Ops[CurNum] = 3
        
        if (CurNum%2 == 0):
            CurOp = NumOps[int(CurNum/2)] + 1
            if (NumOps[CurNum] > CurOp):
                NumOps[CurNum] = CurOp
                Ops[CurNum] = 2
        #plus 1's case
        CurOp = NumOps[CurNum - 1] + 1
        if (NumOps[CurNum] > CurOp):
            NumOps[CurNum] = CurOp
            Ops[CurNum] = 1

    k = NumOps[n]

    for i in range(k):
      OpSum.append(n)
    k= k-2
    Num = n

    while (Num > 0 and k >=0):
        if (Ops[Num] == 1):
            OpSum[k] = Num - 1
            Num = Num - 1
            k = k - 1

        elif (Ops[Num] == 2):
            OpSum[k] = int(Num / 2)
            Num = int(Num / 2)
            k = k - 1

        elif (Ops[Num] == 3):
            OpSum[k] = int(Num / 3)
            Num = int(Num / 3)
            k = k - 1

    return OpSum


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
