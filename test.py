import os
import utils
# print(os.getcwd())

# with open("dummy_jd.txt","r") as f:
#     context = f.readlines()
#     print(context)   

os.getcwd()
resume_name = "dummy_resume.txt"
js_name = "dummy_jd.txt"

resume_content = utils.read_file(resume_name)
js_content = utils.read_file(js_name)

prompt=f"""find if the candidate matches the job description 
Job description is
```
{js_content}
```
Candidate resume is
```
{resume_content}
```
"""



# jd = "dummy_jd.txt"

# def given_jd(jobd):
#     with open(jobd,"r") as d:
#         criteria = d.readlines()
#         print(criteria)
# given_jd(jd)

