import utils
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate   # ✅ use ChatPromptTemplate

model = OllamaLLM(model="gemma3:4b")

resume_name = "dummy_resume.txt"
jd_name = "dummy_jd.txt"

resume_content = utils.read_file(resume_name)
jd_content = utils.read_file(jd_name)

template = """
You are a HR looking for the perfect match for Job Description your company is looking for
and who should be the perfect or excellent person for that Job. 

Here are the JOB REQUIREMENTS: {job_requirement}

This is the candidate who applied for that role: {applied_candidate}
"""

prompt = ChatPromptTemplate.from_template(template)   # ✅

chain = prompt | model   # ✅ works now

result = chain.invoke({
    "job_requirement": jd_content,
    "applied_candidate": resume_content
})

print(result)
