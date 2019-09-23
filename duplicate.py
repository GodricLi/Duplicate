"""找出列表中重复数字"""


def duplicate(arr):
    """
    从头扫到尾，把不存在集合中的元素添加到集合，存在的即为重复元素，添加到字典，返回
    :param arr:数列
    :return:重复元素的字典
    """
    if not arr or len(arr) <= 1:
        return False
    el = set()
    duplication = {}
    for index, val in enumerate(arr):
        if val not in el:
            el.add(val)
        else:
            duplication[index] = val
    return duplication


if __name__ == '__main__':
    print(duplicate([1, 2, -3, 4, 4, 95, 95, 5, 2, 2, -3, 7, 7, 5]))
