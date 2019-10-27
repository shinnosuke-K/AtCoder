def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    return divisors


divisors = make_divisors(int(input()))
sub_list = []
for i in range(1, len(divisors), 2):
    sub_list.append(divisors[i] - divisors[i-1])

min_index = sub_list.index(min(sub_list))
print(divisors[min_index * 2] + divisors[(min_index+1) * 2 - 1] - 2)