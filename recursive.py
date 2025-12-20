

# def even(n,i=0):
#     if n!=0:
#         print(i*2,end=" ")
#         even(n=n-1,i=i+1)                         # n even numbers
# even(int(input("enter a number: ")))

#output:
# enter a number: 5
# 0 2 4 6 8 







# def even(n,i=0):
#     if n!=0:
#         print((i*2)+1,end=" ")
#         even(n=n-1,i=i+1)                         # n odd number numbers
# even(int(input("enter a number: ")))

# output:
#     enter a number: 5
#     1 3 5 7 9 





# def Fun(n,i=2):
#     if n%i==0 :
#         return True                     #  checking prime number
#     if i * i > n:
#         return False
#     return Fun(n,i=i+1)
        
# res=Fun(5)
# print(res)
        
        
# output
# enter a number:5
# prime

# enter a number:6
# not a prime 
    
    
# def prime_numbers(n, num=2, count=0):           # n prime numbers
    
#     def is_prime(num):
#         for i in range(2,num):
#             if num%i==0:
#                 return False
#                 break
#         else:
#             return True
#     if count==n:
#         return
#     if is_prime(num):
#         print(num,end=" ")
#         prime_numbers(n, num + 1, count + 1)
#     else:
#         prime_numbers(n, num + 1, count)
        
# prime_numbers(int(input("enter a  number :")))





# enter a  number :5
# 2 3 5 7 11 
# def fact(n,i=1):                  # factorial of a given number with using recursive function
#     if n!=0:
#         return n*fact(n=n-1)
#     return i
# print(fact(int(input("enter a number: "))))

# enter a number: 5
# 120
# def is_strong_number(num, total=0):              
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n - 1)

#     if num == 0:
#         return total == 0
#     else:
#         digit = num % 10
#         return is_strong_number(num // 10, total + factorial(digit))
    
# res=is_strong_number(145)
# print(res)


# # Test the function
# number = 145
# if is_strong_number(number):
#     print(f"{number} is a strong number")
# else:
#     print(f"{number} is not a strong number")


# def f(n):
#     print(n,end='')                       # some pgr
    
#     if n>0:
#         f(n=n-1)
#         print(n,end="")
            
# f(5)
#outPut:54321012345



# l=[[1,2],[3,4],[5,6]]

# def f(l):                                     #sum of the list elements
#     t=0
#     for i in l:
#         if type(i)==list:        
#             t=t+f(i)
#         else:
#             t+=i
#     return t
# print(f(l))

# outPut:21



# def even(n):
#     if n>0:
#         even(n-1)
#         print((n-1)*2,end=" ")

# even(5)



# def r(n,s=0):        #counting the numbers 
#     if n>9:
#         while n>0:
#             t=n%10
#             s=t+s
#             n=n//10
#         if s>9:
#             return r(n=s)
#         else:
#             return s
# print(r(5643))

# 5+6+4+3=18-->1+8=9

#output=9



# def is_strong_number(num, total=0, original=None):
#     if original is None:
#         original = num
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n - 1)
#     if num == 0:
#         return total == original 
#     else:
#         digit = num % 10 
#         return is_strong_number(num // 10, total + factorial(digit), original)

# res = is_strong_number(145)
# print(res) 


# x=[1,2,3,[4,5],[6,7,8],9]

# def fun(x,l=[]):

#     for i in x:
#         if type(i)==list:
#             fun(i)
#         else:
#             l+=[i]
#     return l
# print(fun(x))
            

# def feb_series(n,a=0,b=1):
#     if a==0:
#         print(a,b,end=" ")
#     if n!=2:
#         c=a+b
#         print(c,end=" ")
#         feb_series(a=b,b=c,n=n-1)
# feb_series(7)


import json
import os
from groq import Groq   # or any LLM client you use

client = Groq(api_key=os.environ.get('GROQ_API_KEY'))


def generate_interview_blueprint(
    parsed_jd: dict,
    mandatory_questions: list | None,
    total_questions: int | None
) -> dict:
    """
    Creates ONE interview blueprint per JD using LLM.
    """

    system_prompt = """
You are an expert technical interviewer and hiring manager.

Your task is to create ONE interview blueprint.

CRITICAL CONSTRUCTION RULES (MUST FOLLOW EXACTLY) and creaate no of Blue-print Questions or topic based on input:

The number of blueprint items must be created strictly based on the input provided.

PHASE 1: SELF INTRODUCTION
- The first item is always:
  - order = 1
  - type = "self_intro"

PHASE 2: HR MANDATORY QUESTIONS
- If HR mandatory questions are provided:
  - Add ALL HR questions immediately after self_intro
  - HR questions MUST appear contiguously
  - HR questions MUST NOT appear after any technical question
  - Do NOT change the question text
  - Do NOT change their order
  - Do NOT merge, move, or rewrite HR questions
- Each HR question must be a separate item
- HR questions are same for all students

PHASE 3: TECHNICAL QUESTIONS (TOPICS ONLY)
- Add ONLY technical items after ALL HR questions
- Technical items must be:
  - Derived strictly from the Job Description
  - Theoretical only (NO coding)
  - Difficulty must always be "medium"
- Prioritize core role skills over cross-domain awareness skills

COUNT & LIMIT RULES (VERY IMPORTANT)
--------------------------------------------------

- Total questions =
  1 (self_intro)
  + number_of_hr_questions
  + number_of_technical_questions

- NEVER exceed the total_questions value provided
- HR questions can NEVER be removed, even if slots are limited

COUNT RULES:

- Total questions = 1 (self_intro) + number_of_hr_questions + number_of_technical_questions
- NEVER exceed the total_questions provided.
- If slots are limited, MERGE technical skills.
- NEVER remove or relocate HR questions.

STRICT OUTPUT RULES:
- Output ONLY valid JSON
- No explanations
- No comments
- No extra keys
- Order values must be continuous (1,2,3,4...)

NOTE : generate the number od Question based on user input like  number of Questiond wanted 
Exception:
- HR mandatory questions MUST include the exact question text provided by HR.

Respond in this JSON format:
{
  "blueprint_name": "<STRING: Company + Role + Interview Blueprint>",

  "structure": [
    {
      "order": sno,
      "type": "self_intro"
    },

    

    {
      "order": sno,
      "type": "technical",
      "topic": "<CORE SKILL / SUBJECT>",
      "difficulty": "medium"
    },

    {
      "order": sno,
      "type": "technical",
      "topic": "<CORE SKILL / SUBJECT>",
      "difficulty": "medium"
    },


"""

    user_prompt = {
        "parsed_job_description": parsed_jd,
        "mandatory_questions": mandatory_questions or [],
        "number of Questiond wanted ": total_questions
    }

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # example, choose your model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_prompt)}
        ],
        temperature=0
    )


    blueprint = json.loads(response.choices[0].message.content)
    return blueprint
mandatory_questions = [
    "Explain your experience with Git workflows",
    "Have you worked on any CI/CD pipelines?"
]


parsed_jd ={
  "company_name": "Upward IQ Solutions",
   "client_name": "Oracle",
   "job_title_or_role": ' ',
   "technical_skills": ["React Js",'Python',"django","Mysql","html",'css','js','bootstrap','restapi'],
   "soft_skills": ' ',
   "experience_required": ' ',
   "job_type": ' ',
   "work_mode": ' ',
   "job_location": ["Hyderabad", "Bangalore", "Chennai"],
   "salary": "3.9 LPA",
   "salary_breakup": {
      "base": 3.9,
      "tenure":  " "
   },
   "education_qualification": "Any",
   "stream_constraint": "" ,
   "passout_year": "2022-2025",
   "percentage_or_cgpa": "80% or 8 CGPA",
   "bond_required": ' ',
   "notice_period": ' ',
   "interview_process": ' ',
   "number_of_openings": ' ',
   "roles_and_responsibilities": [],
   "must_have_skills": [],
   "good_to_have_skills": [],
   "certifications_required": ' ',
   "languages_required": ' ',
   "shift_timings": ' ',
   "work_experience_type": ' ',
   "company_website": ' ',
   "contact_email": ' ',
   "contact_phone": ' ',
   "additional_notes": ' ',
   "extra_information": {
      "salary_range_details": ' ',
      "experience_details": ' '
   }
}
blueprint = generate_interview_blueprint(
    parsed_jd=parsed_jd,
    mandatory_questions=mandatory_questions,
    total_questions=7
)

print(json.dumps(blueprint, indent=2))

