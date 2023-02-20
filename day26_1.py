import random

data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_array = [random.choice(data_array) for _ in range(20)]

print(f'#오늘 판매된 전체 물건(중복O, 정렬X) --> {sell_array}')
sell_array.sort()
print(f'#오늘 판매된 전체 물건(중복O, 정렬O) --> {sell_array}')
sell_product = list(set(sell_array))
print(f'#오늘 판매된 물품 종류(중복x) --> {sell_product}')

idx = 0
i = 0
count_list = []
for i in range(len(data_array)):
    count = 0
    for idx in range (len(sell_array)):
        if data_array[i] == sell_array[idx]:
            count = count + 1

            if idx = len(sell_array):
                count_list.append(data_array[i], count)






print("결산 결과 ==>", count_list)