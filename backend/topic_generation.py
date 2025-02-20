import random
from collections import Counter

# Monologue Topics
monologue_topics = [
    "Travel Experiences: A traveler recounting a memorable trip",
    "Travel Experiences: A traveler sharing tips for planning a vacation",
    "Learning Challenges: A student describing how they overcame difficulties while studying a new subject",
    "Learning Challenges: A teacher explaining strategies to help students succeed in exams",
    "Hobbies and Interests: Someone explaining why they enjoy painting as a creative outlet",
    "Hobbies and Interests: A gamer discussing their passion for competitive esports",
    "Health and Fitness: A fitness enthusiast detailing their daily exercise routine",
    "Health and Fitness: A mental health advocate sharing techniques for managing stress",
    "Environmental Awareness: A speaker reflecting on the importance of protecting endangered species",
    "Environmental Awareness: A community leader discussing ways to reduce plastic waste",
    "Workplace Stories: An employee sharing their experience of adapting to remote work",
    "Workplace Stories: A manager describing how they resolved a team conflict",
    "Personal Growth: A motivational story about setting goals and achieving them despite obstacles",
    "Personal Growth: A speaker reflecting on how they learned resilience after failure",
    "Cultural Traditions: A person describing a meaningful festival celebrated in their culture",
    "Cultural Traditions: A traveler sharing how they experienced a foreign tradition",
    "Everyday Life: A reflection on small but significant moments, like commuting or cooking meals",
    "Everyday Life: A speaker discussing how they find joy in simple routines",
    "Dreams and Aspirations: A young professional talking about their career ambitions",
    "Dreams and Aspirations: A retiree reflecting on dreams they’ve achieved and those still ahead"
]

# Dialogue Topics
dialogue_topics = [
    "Job Interview: A candidate answering questions about their qualifications and work experience",
    "Job Interview: An interviewer providing feedback after a candidate’s response",
    "Customer Service Issue: A customer explaining why they want to return a defective product",
    "Customer Service Issue: A representative offering solutions to resolve a billing error",
    "Travel Planning: Two friends discussing destinations and activities for an upcoming trip",
    "Travel Planning: Family members debating budgets and accommodations for a vacation",
    "Health Consultation: A patient describing symptoms to their doctor during a checkup",
    "Health Consultation: A doctor advising a patient on lifestyle changes to improve their health",
    "Academic Advising: A student asking for guidance on choosing the right courses",
    "Academic Advising: An advisor helping a student create a study plan for exams",
    "Workplace Collaboration: Colleagues brainstorming ideas for a marketing campaign",
    "Workplace Collaboration: Team members addressing a missed deadline and finding solutions",
    "Conflict Resolution: Two coworkers resolving a misunderstanding about project roles",
    "Conflict Resolution: Roommates discussing how to fairly divide household chores",
    "Parent-Child Discussion: A parent giving advice to their child about making responsible decisions",
    "Parent-Child Discussion: A child explaining their perspective on a family rule",
    "Tech Support Call: A frustrated user describing issues with their internet connection",
    "Tech Support Call: A tech expert guiding a user through resetting their device",
    "Real Estate Negotiation: A buyer asking questions about property features and pricing",
    "Real Estate Negotiation: A seller justifying their asking price and negotiating terms"
]

def get_monologue_topic():
    return random.choice(monologue_topics)

def get_dialogue_topic():
    return random.choice(dialogue_topics)