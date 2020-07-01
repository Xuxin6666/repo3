#-*- codeing = utf-8 -*-
#@Time : 2020/6/30 22:51
#@Author : 许鑫
#@File : maopao.py
#@Software : PyCharm

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums


if __name__ == '__main__':
    nums = [12,41,23,4,56,51]
    numl = bubble_sort(nums)
    print(numl)
    for i in range(5):
        print(i)

