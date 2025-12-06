# n=input("enter str: ")
# print("palindrome" if n==n[::-1] else "not a palendrome")                   #palindrome singel line

# n=int(input("enter a nuber: "))
# print("prime" if (n%i!=0 for i in range(2,n)) and n>1 else "not aprime")      #prime in one line

# l=[1,2,3,4,5]
# print("unique" if len(l)==len(set(l)) else "not unique")              #checking unique of list

# import math
# is_strong_number = lambda n: n == sum(math.factorial(int(digit)) for digit in str(n))    #STRONG NUMBER
# print(is_strong_number(int(input("enter anumber :"))))


# l=[3,1,3,2,1,3,5,2,7,4,7,3,4,5,6,8,9,3,5,8]      # geting 1st max and 2nd max numbers

# print(list(set(l))[-1],list(set(l))[-2])
import os
from groq import Groq
import json


def evaluate_resume(resume_text, job_description):
    """
    Evaluates a candidate resume against a Job Description (JD)
    using the ATS Matching Engine prompt.
    Returns:
        {
            "eligible": True/False,
            "reason": "...",            # only when not eligible
            "resume_details": {...}     # full model JSON output
        }
    """

    prompt = f"""
You are a strict ATS Resume–JD Matching Engine.
Output ONLY valid JSON. No explanations.
Always follow deterministic logic.
Do not guess.
If unsure, infer strictly from text.
Extract skills EXACTLY as listed in the JD.
Do not expand skills.
Do not add synonyms.
Do not infer related technologies.


Your tasks:

1. Read the Job Description (JD).
2. Read the Candidate Resume text.
3. Extract eligibility criteria from JD and Resume:
      - Education qualification
      - Stream / Branch
      - Passout year (YOP)
      - Percentage or CGPA

4. Score conversion rules:
      If JD gives percentage but resume gives CGPA → convert resume CGPA to %
      If JD gives CGPA but resume gives percentage → convert resume % to CGPA
      Conversions:
          % → CGPA = % / 10
          CGPA → % = CGPA * 10

5. STRICT EARLY ELIGIBILITY CHECK:
      If ANY of these 4 (education, stream, passout year, percentage/cgpa) do NOT match:
           - eligibility = false
           - failed_criteria = [reason1, reason2, reason3, reason4]
           
6. If all criteria pass:
      - eligibility = true
      - Evaluate skill matching:
            jd_skills = technical_skills + must_have_skills + good_to_have_skills
            Skill Matching Rules:
            1. jd_skills = technical_skills + must_have_skills + good_to_have_skills (unique values)
            2. resume_skills = extracted skill list from resume
            3. matched_skills = intersection of jd_skills and resume_skills (case-insensitive)
            4. skill_match_percentage MUST be computed using:

                skill_match_percentage = (len(matched_skills) / len(jd_skills)) * 100

            5. Extra skills in the resume MUST NOT reduce or increase the percentage.
            6. The model MUST NOT divide by resume skill count.
            7. The model MUST NOT apply weighting, scoring, assumptions, or heuristics.
            8. If len(jd_skills) = 0, then skill_match_percentage = 0.

      - Experience match:
            Compare JD experience_required vs resume experience
            if no experience required in jd ignore this
      -Project Match Calculation:
        - Extract all project titles and descriptions from the resume.
        - Check if each project contains ANY JD skill (case-insensitive).
        - matched_projects_count = number of projects containing ≥1 JD skill
        - total_projects = total number of projects in resume
        - If total_projects > 0:
            project_match_percentage = (matched_projects_count / total_projects) * 100
        Else:
            project_match_percentage = 0

        Overall Match Calculation (STRICT):
        - overall_match_percentage =
                (skill_match_percentage * 0.80)
            + (project_match_percentage * 0.20)

        - The model MUST compute using this exact mathematical formula.
        - DO NOT assume fixed values. DO NOT hallucinate.
        - All percentages must be numbers (no strings).


7. Output JSON ONLY in this structure:

{{
  "eligibility": true,
  "failed_criteria": [],
  "criteria_analysis": {{
      "yop_match": null,
      "education_match": null,
      "stream_match": null,
      "percentage_or_cgpa_match": null,
      "converted_values_used": {{
          "resume_percentage_converted_to_cgpa": null,
          "resume_cgpa_converted_to_percentage": null
      }}
  }},
  "skill_matching": {{
      "jd_skills": [],
      "resume_skills": [],
      "matched_skills": [],
      "skill_match_percentage": %
  }},
  "experience_matching": {{
      "jd_experience": "",
      "resume_experience": "",
      "experience_match": null
  }},
  "overall_match_percentage": %,
  "final_verdict": ""
}}

Use this JD structure while parsing:
{json.dumps(job_description)}

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,  # VERY IMPORTANT
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    raw_output = response.choices[0].message.content
    print(raw_output)

    try:
        model_json = json.loads(raw_output)
    except:
        return {
            "eligible": False,
            "reason": "Model returned invalid JSON",
            "resume_details": {}
        }

    # Build final response
    result = {
        "eligible": model_json.get("eligibility", False),
        "reason": None,
        "resume_details": model_json
    }

    # If criteria failed → send specific reason
    if not result["eligible"]:
        failed = model_json.get("failed_criteria", [])
        if failed:
            result["reason"] = f"Failed criteria: {', '.join(failed)}"
        else:
            result["reason"] = "Eligibility criteria not met"

    return result


dummy_jd = """Company: Upward IQ Solutions
Client: Oracle
Educational Qualification: Any BTech, BSC, or BCA
Stream Constraint: Any CSE/IT stream
Year of Passout: 2022 – 2025
Percentage Constraint: Above 80% or 8 CGPA
Job Location: Hyderabad / Bangalore
Skills: React JS, JavaScript, HTML
Salary: 3.9 LPA"""

dummy_resume = """Name: Rahul Sharma
Email: rahulsharma@example.com
Phone: 9876543210
Education:
B.Tech in Computer Science Engineering
Year of Passout: 2023
CGPA: 9.6
Skills: JavaScript, React JS, HTML, CSS, Python, Git, SQL

"""


print(evaluate_resume(dummy_resume,dummy_jd))