from logger_2 import logger
@logger("log_5.log")
def flat_generator(list_of_lists):  #generator function from HW

    for lists in list_of_lists:
        for item in lists:
            yield item


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
flat_generator(list_of_lists_1)