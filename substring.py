A = [10, 20, 30]  # target = 30
n = len(A)

for s in range(n):
    total_sum = 0
    subarray = []
    for e in range(s, n):
        total_sum += A[e]
        subarray.append(A[e])
        if total_sum == 30:
            print(subarray)
            break

#code for zoho

def char_to_num(c):
    return ord(c) - ord('a') + 1

def num_to_char(n):
    return chr(n + ord('a') - 1)

def find_substrings(n, string):
    result = []
    current_sum = 0
    current_substring = ''
    
    for char in string:
        current_sum += char_to_num(char)
        current_substring += char
        
        while current_sum > n:
            current_sum -= char_to_num(current_substring[0])
            current_substring = current_substring[1:]
        
        if current_sum == n:
            result.append(current_substring)
    
    return result

n = 41
string = "zohocorporation"
substrings = find_substrings(n, string)
print(substrings)



#Java Code

# import java.util.ArrayList;

# public class Main {
#     public static void main(String[] args) {
#         int[] A = {10, 20, 30}; // target = 30
#         int n = A.length;

#         for (int s = 0; s < n; s++) {
#             for (int e = s; e < n; e++) {
#                 int sum = 0;
#                 ArrayList<Integer> al = new ArrayList<>();
#                 for (int i = s; i <= e; i++) {
#                     sum += A[i];
#                     al.add(A[i]);
#                     if (sum == 30) {
#                         System.out.println(al);
#                     }
#                 }
#             }
#         }
#     }
# }
			#subArray 10,20
# 						#subArray 30

# when s=0
# =========
# 1st for true s<3
#    when e=0
#    ========
#    2nd for true e=0, e<3
#      3rd for true i=0, 0<=0 
#        printingA[0]- 10
#         i++, so i=1;
# 	i=1,1<=0 false

#    when e=1
#    ========

# 2nd for e=1, e<3
#      3rd for i=0; 0<=1 true
# 	printing A[0]-10
#      3rd for i=1,1<=1 true
# 	printing A[1]-20
# 	i=2; 2<=1 false 
   
#     when e=2
#     ========
#    2nd for e=2, e<3
#      3rd for i=0; 0<=2 true
# 	printing A[0]-10
#      3rd for i=1,1<=2 true
# 	printing A[1]-20
#      3rd for i=2; 2<=2 true
# 	printing A[i]-30
# 	 i=3,3<=2 false

#     when e=3
#    ==========
#    2nd for e=3 2<3 false

# now becomes s=1
# ===============
#     when e=1
#     ========
#    2nd for e=1 1<3 true	
#      3rd for i=1; 1<=1 true
# printing A[i] -20
# 	i=2; 2<=1 false
#     when e=2
#    ==========
#    2nd for e=2 2<3 true
#      3rd for i=1; 1<=2 true
# 	printing A[i] -20
#      3rd for i=2; 2<=2 true
# 	printing A[i] - 30
# 	i=3; 3<=2 false
#    when e=3
#    ==========
#    2nd for e=3 2<3 false 

# now s=2
# =======
# printing- 30
# 10,
# 20,
# 30,
# 10,20
# 20,30
# 10,20,30