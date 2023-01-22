# listの中身をスペース区切りで出力する
output_list = [1,2,3,4]
output = ' '.join(list(map(str,output_list)))
print(output)