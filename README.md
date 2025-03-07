# 🌍 AI Travel Planner

An AI-powered travel assistant that helps users plan their trips by providing destination guides, travel logistics, and personalized itineraries using **CrewAI, LangChain, and Groq LLMs**.

## 🚀 Features
- **Local Guide Recommendations**: Provides personalized attractions, food spots, and events.
- **Travel Logistics Expert**: Offers travel-related details such as accommodation, costs, transportation, and visas.
- **AI-Powered Trip Planner**: Generates structured travel itineraries based on user interests.
- **Web Search Integration**: Fetches real-time travel information via Tavily Search.
- **Multilingual Support**: Responds in French for French-speaking destinations.

## 🛠 Tech Stack
- **[CrewAI](https://github.com/joaomdmoura/crewai)** – Multi-agent orchestration
- **[LangChain](https://www.langchain.com/)** – AI framework for LLMs
- **[Groq API](https://groq.com/)** – Llama-3 AI model
- **[Tavily Search](https://tavily.com/)** – Web search tool for real-time information

- **Streamlit** – UI (optional for front-end deployment)

---

## 📌 Setup Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/travel-ai-planner.git
cd travel-ai-planner
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```ini
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

#

### 5️⃣ Run the Streamlit App (Optional UI)
```sh
streamlit run app.py
```

---

## 📚 Usage
### **🔹 Travel Experts (CrewAI Agents)**
1. **Guide Expert** 🏙️ – Recommends local attractions & experiences.
2. **Location Expert** ✈️ – Provides travel logistics (accommodation, visa, etc.).
3. **Planner Expert** 🗺️ – Combines data into a structured itinerary.

### **🔹 Example API Request**
#### **POST `/chat`**
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "Plan a trip for me.",
  "messages": ["I want to visit Paris in April."],
  "allow_search": true
}
```

---

## 📜 Task Descriptions
### **🔹 Location Task**
- Provides travel-related info including **cost of living, visa, transport, and weather**.
- Responds in **French** if the destination is in a French-speaking country.
- **Output:** `city_report.md`

### **🔹 Guide Task**
- Generates **attractions, food recommendations, and event lists**.
- Tailored based on user **interests**.
- **Output:** `guide_report.md`

### **🔹 Planner Task**
- Combines all info into a **detailed travel plan**.
- Includes **city introduction, daily plan, expenses, and tips**.
- **Output:** `travel_plan.md`

---

## 🛠 Future Improvements
- ✅ Integrate AI-generated **hotel & flight booking recommendations**
- ✅ Improve **budget estimation** for travelers
- ✅ Add **multi-destination** trip planning
- ✅ Deploy on **Hugging Face Spaces**

---

## 🤝 Contributing
Feel free to **fork** this repo, open issues, or submit PRs! 🚀

---

## 📜 License
This project is licensed under the **MIT License**.

---

💡 **Made with ❤️ by AI Travel Enthusiasts!**

