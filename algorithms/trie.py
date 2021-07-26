
ans = 0

class node:
    def __init__(self):
        self.child = [None]*26
        self.val = 1
        self.leaf = False

class trie:

    def __init__(self):
        self.root = node()

    def insert(self,s):
        temp = self.root
        for i in s:
            if not temp.child[ord(i)-97] : 
                temp.child[ord(i)-97] = node()
                temp = temp.child[ord(i)-97]
            else:
                temp = temp.child[ord(i)-97]
                temp.val+=1

    def search(self,s):
        temp = self.root
        for i in s :
            if temp.child[ord(i)-97] == None:
                return False
            else:
                temp=  temp.child[ord(i)-97]
        return True


def dfs(node,lev):
    global ans
    #print("first" + str(lev))
    cnt =0 
    for i in range(26):
        if node.child[i] != None:
            #print("into child")
            cnt+=dfs(node.child[i],lev+1)
            node.child[i] = None

    node.val-=cnt

    #print("second" + str(lev))
    if node.val >= 2:
        # print("asd")
        # print("third" + str(lev))
        temp = (node.val//2)
        cnt += temp*2
        ans += (temp*(lev//2)*(lev//2))

    return cnt

def main():
    global ans
    q = int(input())
    for T in range(q):
        ans = 0
        t = trie()
        n = int(input())
        for i in range(n):
            st = input().strip()
            rest = st[::-1]
            newst = ""
            for j in range(len(st)):
                newst = newst+st[j]+rest[j]
            t.insert(newst)
        #print(t.root.val)
        dfs(t.root,0)
        print(ans)
    
    

if __name__ == '__main__': 
    main() 