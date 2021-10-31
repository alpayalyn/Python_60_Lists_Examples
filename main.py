#code with me 60Lists appearences might help
#---------------------------------------------------------------------------------------------------#
print("------1st------")
a_list = [1 ,2, 3, 'a', 'b', 'c']
print(a_list)

#---------------------------------------------------------------------------------------------------#
print("------2nd------")
#Iterating 2++ lists simultaneously

environment = ['mountain', 'river', 'lake']
name = ['John', 'Elizabeth', 'Simon']

zipped_tuple = zip(environment, name)

for element in zipped_tuple:

    print(element)
#---------------------------------------------------------------------------------------------------#
print("------3rd------")
#Lists or dictionaries to use for storing datas.

#use if you want to be able to store duplicates.

list1 = [1, 2, 3, 3, 4, 5, 6]

dict1 = {'friend': 1, 'stranger': 2, 'nobody': 3} # as you can follow there is only one way you can call those values. And you can not use the keys twic

#---------------------------------------------------------------------------------------------------#

#Append and extend difference?
print("------4th------")

a = [1,2,3]

a.append(4)
a.append([5,6])
print(a)

b = [1,2,3]
b.extend([5,6])
print(b)

#Extend include 2nd lists members as its own members not like append.
#---------------------------------------------------------------------------------------------------#
print("------5th------")

#A list doesnt Have to be Homogenous, you can include a list into a list, or str, or int

list1 = ['alpay', 24, ['tester', 'insider'], 0.3]
print(list1)

#---------------------------------------------------------------------------------------------------#
print("------6th------")

#1DEL, 2REMOVE, 3POP

list1 = [1, 2, 3, 4, 5, 6]

del(list1[4])
print(list1)

list1.remove(2)
print(list1)

#The difference between pop and del is that pop returns the popped element. This allows using a list like a stack.

b = list1.pop(1)
print(b)

#---------------------------------------------------------------------------------------------------#
print("------6th------")
