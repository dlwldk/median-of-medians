def find_median_five(L):
   mid = int(len(L)/2)
   max1, min1 = L[1], L[0]
   if L[0] > L[1]: max1, min1 = L[0], L[1]
   max2, min2 = L[-2], L[-1]
   if L[-1] > L[-2]: max2, min2 = L[-1], L[-2]

   if max1 > max2:
      if L[mid] > min1: max1 = L[mid]
      else:
         max1 = min1
         min1 = L[mid]
   else:
      if L[mid] > min2: max2 = L[mid]
      else:
         max2 = min2
         min2 = L[mid]

   if max1 > max2: return max2 if max2 > min1 else min1
   else: return max1 if max1 > min2 else min2

def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
   if len(L) == 1: # no more recursion
      return L[0]
   i = 0
   A, B, M, medians = [], [], [], []
   while i+4 < len(L):
      medians.append(find_median_five(L[i: i+5]))
      i += 5
   if i < len(L) and i+4 >= len(L):
      length = len(L)-i
      if length == 1:   medians.append(L[i])
      elif length == 2:   medians.append(max(L[i],L[i+1]))
      else:   medians.append(find_median_five(L[i:]))

   mom = MoM(medians, int(len(medians)/2))
   for v in L:
      if v < mom: A.append(v)
      elif v > mom: B.append(v)
      else: M.append(v)

   if len(A) >= k:   return MoM(A,k)
   elif len(A)+len(M) < k:   return MoM(B, k-len(A)-len(M))
   else: return mom

n, k = map(int, input().split())# n과 k를 입력의 첫 줄에서 읽어들인다
L = list(map(int, input().split()))# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
print(MoM(L, k))
