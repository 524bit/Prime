def isPrime(num):
  if num <= 1:
    return False
  root_val = round(num ** 0.5)
  for i in range(2, root_val+1):
    if num % i == 0:
      return False
  return True

primes = []
m_primes = []
MAX_NUM = 100000000 #멕스 넘버 수정( 원하는 만큼 )

print('''2p-1
finding the Mersen prime...
Please wait''')

for i in range(2, MAX_NUM):
  if isPrime(i):
    primes.append(i)
print(primes, "\n")