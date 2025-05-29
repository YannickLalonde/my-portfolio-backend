from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/projects")
def get_projects(request):
    # In a real app, you'd fetch this from your database
    projects = [
        {"id": 1, "name": "Portfolio Website", "description": "My personal portfolio showcasing fullstack skills.",
         "tech": ["Next.js", "React", "MUI", "Django-Ninja", "PostgreSQL"]},
        {"id": 2, "name": "E-commerce Platform", "description": "A scalable e-commerce solution.",
         "tech": ["Django", "React", "Stripe", "PostgreSQL"]},
        # Add more projects here
    ]
    return projects


@api.get("/skills")
def get_skills(request):
    skills = [
        {"category": "Frontend", "name": "React", "level": 90},
        {"category": "Frontend", "name": "Next.js", "level": 85},
        {"category": "Frontend", "name": "Material UI", "level": 80},
        {"category": "Backend", "name": "Django", "level": 95},
        {"category": "Backend", "name": "Django-Ninja", "level": 90},
        {"category": "Database", "name": "PostgreSQL", "level": 85},
        {"category": "DevOps", "name": "Vercel", "level": 75},
        {"category": "Languages", "name": "Python", "level": 95},
        {"category": "Languages", "name": "TypeScript", "level": 80},
    ]
    return skills


# Example for a contact form submission
@api.post("/contact")
def submit_contact(request, name: str, email: str, message: str):
    # In a real app, you'd save this to the database or send an email
    print(f"Received contact message from {name} ({email}): {message}")
    return {"success": True, "message": "Message received!"}
