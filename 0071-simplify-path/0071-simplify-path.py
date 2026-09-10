class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        output = []
        i = 0
        arrayDirectories = path.split("/")
        for i  in range (0, len(arrayDirectories)):
                if arrayDirectories[i] == "." or arrayDirectories[i] =="":
                    continue
                if arrayDirectories[i] == "..":
                    if len(output)!=0:
                        output.pop()
                else:
                    output.append(arrayDirectories[i])
        print(output)
        answer = ""
        for dir in output:
            answer+="/"
            answer+=dir
        if answer == "":
            answer = "/"
        return answer




        