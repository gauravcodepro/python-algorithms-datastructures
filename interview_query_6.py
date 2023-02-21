#Marked Lists https://www.interviewquery.com/
#You are given two lists of strings list1 and list2, which are sorted alphabetically in ascending order.
#Implement a function that merges these two lists into one sorted list marking all items from list1 and 
# list2 with characters "1" and "2" respectively at the end of each item and return that list.
#Example:
#Input:
#list1 = ["ball","ninja","plan"]
#list2 = ["cat","egg","zoo"]
#Output:
#def mark_lists(list1,list2) ->
#["ball1","cat2","egg2","ninja1","plan1","zoo2"]
list1 = ["ball","ninja","plan"]
list2 = ["cat","egg","zoo"]
sorted([j for i in ([x,y] for x,y in zip(list1,list2)) for j in i], key=lambda x: x[0])
['ball', 'cat', 'egg', 'ninja', 'plan', 'zoo']