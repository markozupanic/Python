#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
nums1 = [1,2]
nums2 = [3,4]


nums1=nums1+nums2
print(nums1)
zbroj=0
len_liste=0
for i in nums1:
    zbroj+=i
    len_liste+=1
    
print(zbroj/len_liste)







































