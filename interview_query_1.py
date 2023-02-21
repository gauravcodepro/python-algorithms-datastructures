#Merge N Sorted Lists https://www.interviewquery.com/questions
#Given a list of sorted integer lists, write a function sort_lists to create a combined list 
# while maintaining sorted order without importing any libraries or using the 'sort' or 'sorted' functions in Python.
#Example:
#Input:
#lists = [
#[1,2,3,4,5,6],
#[2,5,7,8],
#[3,9,10,12],
#[0,1,2,8]
#]
#Output:
#def sort_lists(lists) -> [0,1,1,2,2,3,3,4,5,5,6,7,8,8,9,10,12]
print([j for i in lists for j in i])
[1, 2, 3, 4, 5, 6, 2, 5, 7, 8, 3, 9, 10, 12, 0, 1, 2, 8]