from Tasks import *
str_q = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
      "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
      "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

new_test = "yJDOmaOpNpcVlXxPXJjSbxjekgfYKApqaVZFCIFUauFniYsjDEhJSprrskgcMXdrSpSXHhENSMYlOAOZ" \
           "OMExXgoWqprIowrrtXtRudBJbkfxYkSjvbjsayovTlYPZHVrjrkTgrZSPXxgOJJHgUIIDFPaUJAHBiGD" \
           "nKPIgoyXYZKwmLPBlrtGjDfIzEStNQigDBxnibYSKAMGaPGgcyOaONQYJGvloMBRsfQWKYbIVENbUMzg"

test1 = "Pig latin is cool"

# file_name = "mess.txt"

# print(2**38)
# print(second_task(str_q))
# print(second_task("map"))
# print(third_task(file_name))

int_list = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]


def snail_best(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a


print(snail_best(int_list))
