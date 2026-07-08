import os
historyfile=os.path.expanduser('~/.zsh_history')
def getrecentdata(lines:int=15):
    if not os.path.exists(historyfile):
        print(f"history file not found at{historyfile}")
        return []
    try:
        with open(historyfile,"r",encoding="utf-8",errors="ignore") as f:
            zshlines=f.readlines()
        recentlines=zshlines[-lines:]
        cleanedpart=[]
        for l in recentlines:
            l=l.strip()
            if ";" in l and l.startswith(":"):
                command=l.split(";",1)[1]
                cleanedpart.append(command)
            elif l:
                cleanedpart.append(l)
        return "\n".join(cleanedpart)
    except Exception as e:
        return f"Error in reading zsh history: {e}"
if __name__=="__main__":
    exhaust=getrecentdata(40)
    print(exhaust)
    