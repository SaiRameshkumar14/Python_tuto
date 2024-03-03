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