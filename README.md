# 🔍 Smart Research Agent

A GPT-4 powered Python agent that takes a research topic from the user, performs a real-time Google search using SerpAPI, and summarizes the results into a beginner-friendly learning guide.

---

## 🚀 Features

✅ Uses GPT-4 to act as a smart research assistant  
✅ Performs live Google searches using SerpAPI  
✅ Summarizes results clearly using LLM reasoning  
✅ Clean Python structure and `.env` for secure API keys  
✅ Beginner-friendly and extensible (memory, interface, etc.)

---

## 🛠️ How to Run This Project

### 📦 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-research-agent.git
cd smart-research-agent

### 2. Setup the Environment

python -m venv venv
.\venv\Scripts\activate  # Use `source venv/bin/activate` on macOS/Linux
pip install -r requirements.txt

### 3. Add API keys
OPENAI_API_KEY=your_openai_key_here
SERPAPI_API_KEY=your_serpapi_key_here


### 4. Run the agent
python main.py

