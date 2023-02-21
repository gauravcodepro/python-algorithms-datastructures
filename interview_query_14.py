#https://www.interviewquery.com/questions/one-element-removed
#One Element Removed
#There are two lists, list X and list Y. Both lists contain integers from -1000 to 1000 and are identical 
# to each other except that one integer is removed in list Y that exists in list X.
#Write a function one_element_removed that takes in both lists and returns the integer that was 
# removed in O(1)O(1) space and O(n)O(n) time without using the python set function.
#Example:
#Input:
#list_x = [1,2,3,4,5]
#list_y = [1,2,4,5]
#one_element_removed(list_x, list_y) -> 3
first approach
[i for i in list(a) if i not in list(b)]
[3]
