class Main:
    def __init__(self):
        self.st = []

    def balPar(self, ch, n):
        if ch == '(' or ch == '{' or ch == '[':
            self.st.append(ch)
        else:
            if not self.st:
                return False
            x = self.st[-1]
            if ch == ')':
                if x == '{' or x == '[':
                    return False
                else:
                    self.st.pop()
            elif ch == '}':
                if x == '(' or x == '[':
                    return False
                else:
                    self.st.pop()
            elif ch == ']':
                if x == '(' or x == '{':
                    return False
                else:
                    self.st.pop()
        return True

    def solve(self, A):
        n = len(A)
        if A[0] == '}' or A[0] == ']' or A[0] == ')':
            return False
        for i in range(n):
            if not self.balPar(A[i], n):
                return False
        if not self.st:
            return True
        return False

# Example usage:
if __name__ == "__main__":
    obj = Main()
    print(obj.solve("({}[]{})"))



#---------------------------------------------------------------------------------------------
    


# import java.util.Stack;
# public class Main {

#     static Stack<Character> st=new Stack<>();
    
#     public static int balPar(char ch,int n){
    
#         if( ch=='(' || ch=='{' || ch=='[' ){
#             st.push(ch);
#         }
#         else{
#             Character ch1=ch;
#             if(st.isEmpty()) return 0;
#             char x=st.peek();
#             switch(ch){
#                 case ')':
                
#                     if(x=='{' || x=='[' ) return 0;
#                     else st.pop();
#                     break;

#                 case '}':
                    
#                     if(x=='(' || x=='[') return 0;
#                     else st.pop();
#                     break;
                    
#                 case ']':
                    
#                     if(x=='(' || x=='{') return 0;
#                     else st.pop();
#                     break;
                
#             }
#         }
#         return 1; 
#     }

#     public static int solve(String A) {
        
#         int n=A.length();
#         if(A.charAt(0)=='}' || A.charAt(0)==']' || A.charAt(0)==')') return 0;
#         for(int i=0;i<n;i++){
            
#             balPar(A.charAt(i),n);

#         }
#         if(st.isEmpty()) return 1;
#         return 0;
#     }
    
#     public static void main(String[] args){
#         System.out.println(solve("({}[]{})"));
#     }
# }