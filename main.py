
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

knowledge = {
    "eligibility": "To apply, you need to have 10+2 with Physics, Math, or CS and at least 60% aggregate.",
    "fees": "Each semester costs ₹46,000, with a one-time application fee of ₹2,800.",
    "start date": "The program starts in June or July 2025.",
    "specializations": "Two tracks: Artificial Intelligence & Cybersecurity (AICS), and Computer Science & Data Analytics (CSDA).",
    "duration": "This is a 3-year full-time Bachelor of Science (Hons.) degree.",
    "placement": "IIT Patna offers 100% internship and placement support for this program.",
    "mode": "The course is delivered in hybrid mode — 80% online + 20% on-campus immersion.",
    "highest package": "₹82.05 LPA (highest across IIT Patna programs).",
    "contact": "📧 Email: info@iitp-cep.in | 📞 Phone: +91-9021156156",
    "course name": "B.Sc (Hons.) in CSDA or AICS, both NEP 2020-compliant IIT Patna programs."
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get('message', '').lower().strip()
    responses = []

    greetings = ["hi", "hello", "hey", "good morning", "good evening", "hii", "helloo"]
    if any(word in msg for word in greetings) and len(msg.split()) <= 4:
        responses.append("Welcome friend 😊 I’m LippyBot, your assistant.")

    if "who are you" in msg or "what do you do" in msg or "your name" in msg:
        responses.append("I’m LippyBot 🤖 — your chatbot assistant for IIT Patna’s B.Sc program.")

    if "admission link" in msg or "how to apply" in msg or "apply" in msg:
        responses.append("📌 You can apply here: https://iitp-cep.in/apply")

    if "email" in msg:
        responses.append("📧 Contact us at info@iitp-cep.in")

    if "phone" in msg or "contact" in msg:
        responses.append("📞 Phone: +91-9021156156")

    if any(phrase in msg for phrase in ["iit patna", "about iit patna", "what is iit patna"]):
        responses.append("🏫 IIT Patna is a top-tier Indian Institute of Technology established in 2008.")

    if any(phrase in msg for phrase in [
        "about the course", "course details", "bsc course", "b.sc course", "bsc program"
    ]):
        responses.append("📘 The B.Sc (Hons.) program has two tracks:")
        responses.append("1. AICS – AI, cybersecurity, ML, ethical hacking.")
        responses.append("2. CSDA – Core CS, DBMS, data analytics, algorithms.")
        responses.append("🧑‍🎓 NEP-compliant, hybrid learning, with internship support.")

    for keyword in knowledge:
        if keyword in msg:
            responses.append(knowledge[keyword])
            break

    if "thank" in msg:
        responses.append("You're very welcome! 😊")

    if "bye" in msg or "goodbye" in msg:
        responses.append("👋 Goodbye! I’m here anytime you need info.")

    if not responses:
        responses.append("Hmm... I’m still learning 🧠. Try asking about eligibility, fees, placements, or IIT Patna.")

    return jsonify(reply=" ".join(responses))

if __name__ == "__main__":
    app.run(debug=True)
