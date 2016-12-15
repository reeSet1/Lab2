def min(arr):
    min_el = arr[0]
    for elements in arr:
        if elements < min_el:
            min_el = elements
    return min_el

def sr_arifm(arr):
    result = 0
    for elements in arr:
        result+=elements
    result/=len(arr)
    return result

a = [2,4,5,6,7,1]
print(min(a))
print(sr_arifm(a))