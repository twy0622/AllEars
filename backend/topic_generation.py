import random
from collections import Counter

# Monologue and Dialogue Topics
monologue_topics = [
    "Travel and Tourism", "Education and Learning", "Hobbies and Leisure", "Health and Well-being",
    "Environment and Nature", "Work and Career", "Personal Growth", "Life Lessons", "Family Dynamics",
    "Cultural Exchange", "Creative Pursuits", "Social Justice", "Technology and Innovation",
    "Everyday Life", "Dreams and Aspirations", "Historical Reflection", "Food and Culture",
    "Mystery and Imagination", "Money and Finance", "Change and Adaptation"
]

dialogue_topics = [
    "Job Interview", "Customer Service", "Travel Planning", "Health Consultation", "Academic Advising",
    "Professional Collaboration", "Conflict Resolution", "Parent-Child Conversation", "Friendship Bonding",
    "Romantic Relationship", "Tech Support Call", "Real Estate Negotiation", "Fitness Coaching",
    "Environmental Debate", "Gaming Strategy", "Podcast Discussion", "Financial Advice",
    "Cultural Exchange", "Creative Collaboration", "Social Media Drama"
]

# Function to simulate random selection and calculate percentages
def analyze_distribution(topics, num_samples=1000):
    # Randomly select topics
    selected_topics = [random.choice(topics) for _ in range(num_samples)]
    
    # Count occurrences of each topic
    topic_counts = Counter(selected_topics)
    
    # Calculate percentages
    total_samples = len(selected_topics)
    percentages = {topic: (count / total_samples) * 100 for topic, count in topic_counts.items()}
    
    return percentages

# Analyze distributions for monologues and dialogues
monologue_percentages = analyze_distribution(monologue_topics)
dialogue_percentages = analyze_distribution(dialogue_topics)

# Print results
print("Monologue Topic Distribution:")
for topic in monologue_topics:
    percentage = monologue_percentages.get(topic, 0)  # Handle cases where topic wasn't selected
    print(f"{topic}: {percentage:.2f}%")

print("\nDialogue Topic Distribution:")
for topic in dialogue_topics:
    percentage = dialogue_percentages.get(topic, 0)
    print(f"{topic}: {percentage:.2f}%")