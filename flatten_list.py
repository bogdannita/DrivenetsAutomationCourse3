def flatten_list(unflattened_list):
    result = []
    for element in unflattened_list:
        if (type(element) is list) or (type(element) is tuple):
            if len(element) == 0:
                result.append(element)
            result += flatten_list(element)
        else:
            result.append(element)
    return result


test_list = ['1','2', (), [],'3', ['4','5','6',['7','8','9'], '10'],['11', '12', '13']]

print(flatten_list(test_list))
