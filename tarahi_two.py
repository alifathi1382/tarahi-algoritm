import numpy as np
import time


def find_max_subarray(arr):
    n = len(arr)
    max_sum = int()
    start_idx = 0
    end_idx = 0

    # بررسی تمام زیرآرایه‌های ممکن
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            # محاسبه مجموع عناصر زیرآرایه [i:j+1]
            for k in range(i, j + 1):
                current_sum += arr[k]
                # print(current_sum)


            # اگر مجموع زیرآرایه فعلی بیشتر از max_sum بود، آن را به‌روز رسانی می‌کنیم
            if current_sum > max_sum:

                max_sum = current_sum

                start_idx = i
                end_idx = j
        print(start_idx)
        print(end_idx)

    # چاپ بزرگترین زیرآرایه
    print(start_idx,'...')
    print(end_idx,'...')
    print("بزرگترین زیرآرایه:", arr[start_idx:end_idx + 1])
    print("بیشترین مجموع:", max_sum)


# مثال استفاده از تابع
# start_time=time.time()
A = np.random.randint(-9, +9, 100)
start_time = time.time()
print(A)

find_max_subarray(A)

print("---%s seconds ---" % (time.time() - start_time))
