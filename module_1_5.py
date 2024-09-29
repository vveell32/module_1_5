# food = ["apple", "coconut", "banana"]
# food.append(True)
# print(food)
# food.extend(["string", 2])
# print(food)
# food.remove("apple")
# print(food)
# print("coconut" not in food)
# print(food[0:2:2])

# tuple_ = 1, 2, 3, 4
# print(tuple_)
# tuple_2 = (1, 2, 3, 4)
# print(tuple_2)

# immutable_var = tuple([1, 8, False, "Car"])
# print("immutable_tuple:", immutable_var,)
# mutable_list = 1, 8, False, "Car"
# print(type(mutable_list))


# immutable_var = 1, 8, False, "car"
# tuple_ = 1, 8, False, "car"
# immutable_var = tuple_
# print("immutable_tuple:", immutable_var)
# ==============================================================================

immutable_var = ([1, 8], False, "car")
print(type(immutable_var))
print(immutable_var)
# immutable_var[0][1] = 16 Возможно_поменять_элемент_списка_из_состава_кортежа
# immutable_var[2] = 16 Не_поддерживается_обращение_по_элементам_кортежа
# immutable_var[3] = True Не_поддерживается_обращение_по_элементам_кортежа
mutable_list = [1, 8, False, "car"]
print(type(mutable_list))
mutable_list[3] = "bike"
print(mutable_list)


