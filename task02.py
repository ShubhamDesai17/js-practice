import requests
from collections import Counter
response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
print(response)

data=response.json()
pr_creators={}
for i in range(len(data)):
    creator=data[i]["user"]["login"]
    if creator in pr_creators:
        pr_creators[creator]+=1
    else:
        pr_creators[creator]=1

print(pr_creators)

dict=pr_creators

for creator, count in pr_creators.items():
    print(f"{creator}:{count} pull requests")


