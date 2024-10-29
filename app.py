import openai

# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

def analyze_cv(cv_text):
    system_prompt = (
        "Analyze the provided CV to identify key skills, experiences, and qualifications relevant to software development roles. "
        "Based on this analysis, recommend the most suitable role from the following profiles: "
        "1. Apprentice Developer: Learns programming skills while shadowing others, works with code and tests. "
        "2. Junior Developer: Delivers software components under guidance, proficient in testing. "
        "3. Developer: Develops software to meet user needs, writes clean, secure code. "
        "4. Senior Developer: Plans and leads development, integrates software into services. "
        "5. Senior Developer - Management: Focuses on team management and process optimization. "
        "6. Lead Developer: Provides technical leadership, promotes good practices. "
        "7. Lead Developer - Management: Manages processes and leads service improvements. "
        "8. Principal Developer: Leads development across multiple teams, serves as a technical expert. "
        "9. Principal Developer - Management: Combines technical expertise with management responsibilities. "
        "Your analysis should focus on matching the candidate's experiences with the responsibilities and skills outlined for each role."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": cv_text}
        ],
        max_tokens=150
    )

    return response.choices[0].message['content']

def get_role_details(role):
    """Fetch detailed context for the specific role type."""
    role_profiles = {
        "Apprentice Developer": "Learns programming skills while shadowing experienced developers. Engages in coding and testing under supervision, emphasizing a test-driven approach.",
        "Junior Developer": "Delivers software components with guidance, gains proficiency in testing, and begins mentoring others. Responsible for understanding security and user needs.",
        "Developer": "Develops software to meet user needs, writes clean and secure code, and mentors juniors. Responsible for maintaining service components and identifying production issues.",
        "Senior Developer": "Plans and leads development on multiple stories. Integrates software into complete services, mentors juniors, and focuses on improving system resilience.",
        "Senior Developer - Management": "Similar responsibilities as the Senior Developer, but with a focus on team management and optimizing processes.",
        "Lead Developer": "Provides technical leadership, identifies appropriate technologies, and promotes good practices within the team. Guides team collaboration and knowledge sharing.",
        "Lead Developer - Management": "Manages team processes, optimizes development practices, and leads service improvements while ensuring effective standards implementation.",
        "Principal Developer": "Leads and plans development across multiple teams, serving as a technical expert. Facilitates collaboration and capability development across teams.",
        "Principal Developer - Management": "Combines deep technical expertise with management responsibilities, guiding strategic initiatives and driving technology adoption."
    }
    return role_profiles.get(role, "Role not found.")

def refine_recommendation(role):
    """Refine the recommendation based on specific role context."""
    context = get_role_details(role)
    return f"The recommended role is '{role}'. Here is more context: {context}"

# Example CV input (replace with actual CV content)
cv_input = """
John Doe
Software Engineer with 5 years of experience in web development, 
proficient in Python, JavaScript, and React. 
Led a team of 3 developers to create a highly scalable application.
Strong understanding of Agile methodologies and mentoring junior staff.
"""

# Step 1: Analyze the CV
recommended_role = analyze_cv(cv_input)

# Step 2: Refine the recommendation
refined_output = refine_recommendation(recommended_role)

print(refined_output)
