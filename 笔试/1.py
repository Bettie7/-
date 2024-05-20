def subsequence(source, target):
    sub_count = 0
    target_index = 0
    len_source = len(source)
    len_target = len(target)
    # 检查所有的目标字符串
    while target_index < len_target:
        curr_index = target_index
        # 检查源字符串
        for src_index in range(len_source):
            if curr_index < len_target and source[src_index] == target[curr_index]:
                curr_index += 1
        # 找不到匹配字符串
        if curr_index == target_index:
                return -1
        target_index = curr_index
        sub_count += 1
    return sub_count
