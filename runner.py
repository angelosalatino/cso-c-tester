#!/usr/bin/env python
# coding: utf-8

# # CSO Classifier Runner
# 
# To effectively run this script:
#     
# * open a terminal
#     
# * in this folder run ```source env/bin/activate```
#     
# * then ```python RunnerStanford.py```

# In[ ]:


from cso_classifier import CSOClassifier
import json
import datetime;


# In[ ]:


with open("sample_data_acm_cleaned.json","r") as fr:
    papers = json.load(fr)


# In[ ]:


cc = CSOClassifier(modules = "both", enhancement = "all", explanation = True)
results = list()
for pos, paper in enumerate(papers):

    t_paper = dict()
    t_paper["title"] = paper["title"]
    t_paper["abstract"] = paper["abstract"]
    t_paper["keywords"] = str(paper["keywords"])
    print(pos, paper["link"])
    class_paper = cc.run(t_paper)
    results.append({**paper, **class_paper})
        


# In[ ]:


results_file = f"./sample_data_acm_cleaned_classified{datetime.datetime.now()}.json"
with open(results_file, "w") as fw:
    json.dump(results, fw)

