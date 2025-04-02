def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    insieme = original_set - set(elements_to_remove)
    return insieme

print(remove_elements({5, 6, 7}, [7, 8, 9]))