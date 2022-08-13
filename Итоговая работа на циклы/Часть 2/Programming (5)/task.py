n = int(input())
d3, d0d5, last_d, last_d_count = 0, 0, n % 10, 0
sum_over_5, mul_over_7, chetn = 0, 1, 0
while n > 0:
    d3 += n % 10 == 3
    d0d5 += n % 10 == 0 or n % 10 == 5
    last_d_count += n % 10 == last_d
    chetn += (n % 10) % 2 == 0
    if n % 10 > 5:
        sum_over_5 += n % 10
    if n % 10 > 7:
        mul_over_7 *= n % 10
    n //= 10
print(d3, last_d_count, chetn, sum_over_5, mul_over_7, d0d5, sep='\n')
