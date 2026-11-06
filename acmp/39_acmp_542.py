dec_num = int(input())
bin_num_str = bin(dec_num)[2:]
bin_num_str = bin_num_str[::-1]
dec_num_bm = int(bin_num_str, 2)

print(dec_num_bm)
