import json
from textblob import TextBlob
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

def load_target_data():
    """Loads target profile from JSON file."""
    try:
        with open('target_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.RED + "[ERROR] 'target_data.json' not found!")
        return None

def analyze_psychology(posts):
    """
    Analyzes tweets to determine Sentiment (Mood) and Emotional Triggers.
    Returns: Average Polarity Score and List of Triggers.
    """
    total_polarity = 0
    keywords = []

    print(Fore.CYAN + "\n[SYSTEM] Scanning digital footprint...")
    
    for post in posts:
        analysis = TextBlob(post['text'])
        polarity = analysis.sentiment.polarity
        total_polarity += polarity
        
        # Keyword Analysis (Simulating Psychological Profiling)
        text_lower = post['text'].lower()
        
        # Exhaustion Triggers
        if "exhaustion" in text_lower or "tired" in text_lower or "break" in text_lower:
            keywords.append("Burnout / Fatigue")
        
        # Anger Triggers
        if "angry" in text_lower or "fix this" in text_lower or "quit" in text_lower:
            keywords.append("High Anger / Frustration")
        
        # Financial Triggers
        if "paid" in text_lower or "wages" in text_lower or "bills" in text_lower or "wallet" in text_lower:
            keywords.append("Financial Anxiety")

    avg_polarity = total_polarity / len(posts)
    return avg_polarity, list(set(keywords))

def generate_risk_report(target_name, polarity, triggers):
    """
    Generates a 'Behavioral Threat Intelligence Report'.
    Focuses on defensive risk assessment rather than attack generation.
    """
    print(Fore.YELLOW + "\n" + "="*60)
    print(Fore.YELLOW + f"🧠 PSY-HUNTER: BEHAVIORAL THREAT INTELLIGENCE")
    print(Fore.YELLOW + f"👤 TARGET IDENTITY: {target_name}")
    print(Fore.YELLOW + "="*60)

    # 1. MOOD ANALYSIS
    print(f"\n{Fore.WHITE}📊 EMOTIONAL BASELINE SCORE: {polarity:.2f}")
    
    current_mood = ""
    risk_score = 0
    
    if polarity < -0.1:
        current_mood = "NEGATIVE / STRESSED 😡"
        risk_color = Fore.RED
        risk_score = 85
    elif polarity > 0.1:
        current_mood = "POSITIVE / RELAXED 😌"
        risk_color = Fore.GREEN
        risk_score = 20
    else:
        current_mood = "NEUTRAL / BALANCED 😐"
        risk_color = Fore.BLUE
        risk_score = 40

    print(f"Detected Mood State: {risk_color}{current_mood}")

    # 2. VULNERABILITY TRIGGERS
    print(f"\n{Fore.WHITE}🎯 DETECTED PSYCHOLOGICAL VULNERABILITIES:")
    if triggers:
        for trigger in triggers:
            print(f"   - {Fore.RED}[CRITICAL] {trigger}")
    else:
        print("   - No significant emotional triggers detected.")

    # 3. PREDICTIVE ATTACK VECTORS (The "Why it matters" part)
    print(f"\n{Fore.WHITE}🛡️ PREDICTED PHISHING VECTORS (RISK ANALYSIS):")
    
    if "Financial Anxiety" in triggers:
        print(f"{Fore.RED}⚠️ ALERT: Target is highly vulnerable to 'Payroll', 'Bonus', or 'Invoice' scams.")
    if "High Anger / Frustration" in triggers:
        print(f"{Fore.RED}⚠️ ALERT: Target is likely to click on 'Complaint Resolution' or 'Urgent Service Restore' links.")
    if "Burnout / Fatigue" in triggers:
        print(f"{Fore.RED}⚠️ ALERT: Cognitive fatigue detected. Attention span is low; prone to accidental clicks.")

    print(f"\n{Fore.MAGENTA}>>> TOTAL HUMAN VULNERABILITY SCORE: {risk_score}/100")
    print(Style.RESET_ALL)

# Main Execution Loop
if __name__ == "__main__":
    data = load_target_data()
    
    if data:
        polarity, triggers = analyze_psychology(data['recent_posts'])
        generate_risk_report(data['real_name'], polarity, triggers)