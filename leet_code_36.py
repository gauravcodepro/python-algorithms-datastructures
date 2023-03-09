#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#Find the Index of the First Occurrence in a String
#Given two strings needle and haystack, return the index of the first 
#occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.
import re
[i.start() for i in re.finditer('sad', haystack)][:1]
[0]