#!/usr/bin/env python3
"""
快速排序算法 (Quick Sort)
时间复杂度: 平均 O(n log n), 最坏 O(n²)
空间复杂度: O(log n) - 递归栈
"""

def quick_sort(arr):
    """
    快速排序 - 返回新数组 (不修改原数组)
    
    Args:
        arr: 待排序的列表
        
    Returns:
        排序后的新列表
    """
    if len(arr) <= 1:
        return arr
    
    # 选择基准值 (这里选择中间元素)
    pivot = arr[len(arr) // 2]
    
    # 分区
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序左右分区
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    快速排序 - 原地排序 (修改原数组)
    使用 Lomuto 分区方案
    
    Args:
        arr: 待排序的列表
        low: 起始索引
        high: 结束索引
        
    Returns:
        排序后的原列表 (引用)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区并获取基准值的最终位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序左右子数组
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Lomuto 分区方案
    
    Args:
        arr: 待分区的列表
        low: 起始索引
        high: 结束索引
        
    Returns:
        基准值的最终位置索引
    """
    # 选择最后一个元素作为基准
    pivot = arr[high]
    i = low - 1  # i 是小于 pivot 的区域的最后一个索引
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准值放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试示例
if __name__ == "__main__":
    # 测试数据
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 9, 1, 5, 6],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 7, 5, 3, 1],
    ]
    
    print("=" * 50)
    print("快速排序算法测试")
    print("=" * 50)
    
    for i, test in enumerate(test_cases, 1):
        # 测试返回新数组的版本
        original = test.copy()
        sorted_arr = quick_sort(test)
        print(f"\n测试 {i}:")
        print(f"  原数组: {original}")
        print(f"  排序后: {sorted_arr}")
        
        # 测试原地排序版本
        test2 = original.copy()
        quick_sort_inplace(test2)
        print(f"  原地排序: {test2}")
        
        # 验证结果
        assert sorted_arr == test2 == sorted(original), "排序结果错误!"
    
    print("\n" + "=" * 50)
    print("所有测试通过! ✓")
    print("=" * 50)
