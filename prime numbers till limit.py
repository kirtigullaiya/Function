def prime_numbers(limit):
    i=2
    while i<=limit:
        j=2
        while j<=i:
            if i%j==0:
                break
            # print(i)
            # j+=1
            else:
                print(i)
            j+=1
        i+=1
        # print(i)
prime_numbers(20)