# 🤖 Multiple Agent AI Assistant

This project demonstrates a **multi-agent AI assistant** system using **Python**, **Chainlit**, and **OpenAI SDK**. It allows seamless interaction with multiple AI agents to handle diverse tasks such as answering questions, generating content, and assisting with **web development** queries.

---

## 🚀 Features

- 🧠 Multiple LLM agents for different tasks
- 🌐 Web-based interface with Chainlit
- 🔄 Intelligent Handoff between agents
- 🛠️ Built with Python and OpenAI SDK
- 💬 Real-time chat interface
- 📦 Easy to install and run locally

---

## 📡 What is Handoff?

**Handoff** (also known as **handover**) refers to the **automatic switching between agents** based on the user’s need or the task type.

In this project:

- The system decides **which agent is best suited** to handle a specific prompt.
- For example, a **WebDev Agent** answers web development queries, while a **Content Agent** handles creative writing.
- The "handoff" happens **behind the scenes**, so the user experiences **seamless support** as if talking to a single intelligent assistant.

This mirrors how handoff works in cellular networks (switching between towers) or Apple devices (switching tasks between iPhone/Mac/iPad).

### 🧠 Specialized AI Agents
- Custom AI agents designed to assist in specific domains:
  - **💻 WebDev Agent** – Helps build and debug front-end web apps using HTML, CSS, JavaScript, and React.
  - - 📱 **AppDev Agent** – Helps plan and code mobile apps 
  - **📈 Marketing Agent** – Suggests marketing strategies, writes promotional content, improves SEO, and generates ads.
 
### 💬 Chat-Based Interface
- Built using **Chainlit** for a sleek, real-time web UI experience.
    

---

## 🧰 Tech Stack

- Python
- Chainlit
- OpenAI SDK
- AsyncIO
- Dotenv

---

## 📦 Installation

 - uv init 
 - uv add chainlit
 - uv add openai-agents python-dotenv
   
▶️ Run the App

To start the Chainlit app:

uv run chainlit run main.py



