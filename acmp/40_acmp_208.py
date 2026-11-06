dec_num = int(input())
bin_num_str = bin(dec_num)[2:]

max_dec_num = dec_num

for i in range(len(bin_num_str)):
    bin_num_str = bin_num_str[-1] + bin_num_str[0:-1]

    dec_num_cur = int(bin_num_str, 2)

    if dec_num_cur > max_dec_num:
        max_dec_num = dec_num_cur


print(max_dec_num)
