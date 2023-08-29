def binarySearch(arr: list, leftidx:int, rightidx:int, target:int) -> int:
    """Recursive function to return index of target element in a given sorted array."""
    if leftidx > rightidx:
        return -1

    middle:int = (leftidx + rightidx) / 2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binarySearch(arr=arr, leftidx=middle, rightidx=rightidx, target=target)
    else:
        return binarySearch(arr=arr, leftidx=leftidx, rightidx=middle, target=target)


if __name__ == "__main__":
    # Array example
    arr = [1, 3, 7, 8, 11, 15, 25]
    result_index = binarySearch(arr=arr, leftidx=0, rightidx=len(arr) - 1, target=11)
    print(type(result_index))
    print(f"In array {arr}, your target element is at index : {result_index}")
    
