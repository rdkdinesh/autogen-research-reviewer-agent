Below is a **GitHub-ready README.md** for your simple **AutoGen + OpenAI 2-Agent Team** project.

# 🤖 AutoGen 2-Agent Team with OpenAI

A simple beginner-friendly **Multi-Agent AI application** built using **Python, Microsoft AutoGen, and OpenAI**.

This project demonstrates how two specialized AI agents can collaborate as a team to understand a user question, create an initial response, review it, and produce an improved answer.

---

## 🚀 Project Overview

This application uses two AI agents:

### 👨‍💻 Agent 1 — Research Agent

The Research Agent:

* Understands the user's question
* Creates the initial response
* Explains technical concepts
* Provides examples
* Performs the first level of reasoning

### 🔍 Agent 2 — Reviewer Agent

The Reviewer Agent:

* Reviews the Research Agent's response
* Identifies missing information
* Checks the explanation
* Improves the response
* Produces the final answer

The two agents work together as an **AutoGen Team**.

---

## 🏗️ Architecture

```text
                         USER
                           |
                           |
                           v
                  +----------------+
                  |  AutoGen Team  |
                  +-------+--------+
                          |
             +------------+------------+
             |                         |
             v                         v
      +--------------+          +--------------+
      |   Research   |          |   Reviewer   |
      |    Agent     |          |    Agent     |
      +------+-------+          +------+-------+
             |                         |
             | Initial Answer          |
             +------------+------------+
                          |
                          v
                  +---------------+
                  | Improved Final|
                  |    Answer     |
                  +---------------+
```

---

## 🔄 Agent Workflow

```text
User Question
      |
      v
Research Agent
      |
      | Creates initial answer
      v
Reviewer Agent
      |
      | Reviews and improves
      v
Final Response
```

Example:

```text
User:
Explain RAG architecture in simple terms.

        ↓

Research Agent:
RAG combines information retrieval
with an LLM to generate responses
using retrieved information.

        ↓

Reviewer Agent:
Reviews the explanation and adds
details about embeddings, vector
databases, retrieval and generation.

        ↓

Final Answer
```

---

# 🛠️ Technologies Used

* 🐍 Python
* 🤖 Microsoft AutoGen
* 🧠 OpenAI
* 🔐 Python Dotenv
* 🔄 Multi-Agent Collaboration
* 💬 LLM-based Agent Communication

---

# 📁 Project Structure

```text
autogen-two-agent-openai/
│
├── main.py
│
├── .env
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Prerequisites

Make sure you have:

* Python 3.10+
* OpenAI API key
* Internet connection
* Basic Python knowledge

---

# 🔑 OpenAI API Key

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

Example:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

⚠️ **Never commit your `.env` file to GitHub.**

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 📦 Installation

## Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/autogen-two-agent-openai.git
```

Navigate to the project:

```bash
cd autogen-two-agent-openai
```

---

## Step 2 — Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 📥 Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` contains:

```text
autogen-agentchat
autogen-ext[openai]
python-dotenv
```

---

# ▶️ Step 4 — Run the Application

```bash
python main.py
```

You will see:

```text
Enter your question:
```

Enter a question such as:

```text
Explain RAG architecture in simple terms.
```

---

# 💬 Example Interaction

### User

```text
Explain RAG architecture in simple terms.
```

### Research Agent

```text
RAG stands for Retrieval Augmented Generation.

It combines a retrieval system with a
large language model.

The retrieval system finds relevant
information and provides it to the LLM
before generating the final response.
```

### Reviewer Agent

```text
The explanation is correct.

A more complete explanation should also
mention document chunking, embeddings,
vector databases and similarity search.

The improved explanation is:

RAG is an architecture where documents
are converted into embeddings and stored
in a vector database. When a user asks a
question, relevant chunks are retrieved
and provided to the LLM to generate a
grounded response.
```

---

# 🧠 How AutoGen Works in This Project

The application creates an OpenAI model client:

```python
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)
```

Then the Research Agent is created:

```python
research_agent = AssistantAgent(
    name="research_agent",
    model_client=model_client,
    system_message="""
    You are a Research Agent.
    Create a clear and accurate initial answer.
    """
)
```

The Reviewer Agent is created:

```python
reviewer_agent = AssistantAgent(
    name="reviewer_agent",
    model_client=model_client,
    system_message="""
    You are a Reviewer Agent.
    Review and improve the answer produced
    by the Research Agent.
    """
)
```

Both agents are then added to the team:

```python
team = RoundRobinGroupChat(
    participants=[
        research_agent,
        reviewer_agent
    ],
    termination_condition=termination
)
```

The team receives the user's task:

```python
result = await team.run(
    task=question
)
```

---

# 🔄 Round-Robin Agent Communication

The project uses a round-robin team.

```text
             User
               |
               v
        Research Agent
               |
               v
        Reviewer Agent
               |
               v
        Research Agent
               |
               v
        Reviewer Agent
               |
               v
             STOP
```

The termination condition controls when the conversation ends.

```python
termination = MaxMessageTermination(
    max_messages=4
)
```

This prevents the agents from continuing indefinitely.

---

# 🎯 Why Use Multiple Agents?

Instead of asking one LLM to perform every task, we can divide responsibilities.

```text
Single Agent

User
 |
 v
LLM
 |
 v
Answer
```

versus:

```text
Multi-Agent

User
 |
 v
Research Agent
 |
 v
Reviewer Agent
 |
 v
Improved Answer
```

Each agent has a specialized responsibility.

This pattern can be extended to much larger AI systems.

---

# 🧩 Multi-Agent Design Pattern

The basic pattern demonstrated here is:

```text
              Task
                |
                v
       +----------------+
       | Research Agent |
       +-------+--------+
               |
               v
       +----------------+
       | Review Agent   |
       +-------+--------+
               |
               v
        Final Response
```

This is a simple example of **agent specialization**.

---

# 🌱 Possible Future Enhancements

This project intentionally starts simple.

The architecture can later be extended with:

### 1. More Agents

```text
                    USER
                      |
                      v
               AutoGen Team
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
   Research       Developer       Reviewer
     Agent          Agent           Agent
```

### 2. RAG

Add a Retrieval-Augmented Generation pipeline:

```text
PDF / Documents
      |
      v
Document Loader
      |
      v
Text Splitting
      |
      v
Embeddings
      |
      v
FAISS Vector Store
      |
      v
Research Agent
      |
      v
Reviewer Agent
```

### 3. Tools

Agents can be given tools for:

* Web search
* Database queries
* APIs
* File processing
* Calculations
* Code execution

### 4. Guardrails

Add:

```text
User Input
    |
    v
Input Guardrail
    |
    v
AutoGen Team
    |
    v
Output Guardrail
    |
    v
Final Response
```

### 5. Evaluation

Evaluate:

* Answer correctness
* Relevance
* Completeness
* Hallucination
* Agent collaboration

### 6. Streamlit UI

The command-line interface can later become:

```text
+--------------------------------------+
|       🤖 AutoGen AI Team             |
+--------------------------------------+
|                                      |
| Ask your question:                   |
|                                      |
| [ Explain RAG architecture...... ]   |
|                                      |
|              [ Submit ]              |
|                                      |
+--------------------------------------+
| Research Agent                       |
| ------------------------------------ |
| Initial response...                  |
|                                      |
| Reviewer Agent                       |
| ------------------------------------ |
| Improved response...                 |
+--------------------------------------+
```

---

# 📚 Learning Objectives

After completing this project, you should understand:

* What an AI agent is
* What AutoGen is
* How to create an `AssistantAgent`
* How to connect AutoGen with OpenAI
* How system instructions define agent responsibilities
* How multiple agents collaborate
* How an AutoGen team works
* What round-robin agent communication means
* How termination conditions work
* How multi-agent architecture can be extended

---

# 🔐 Security Notes

Never hard-code API keys:

❌ Don't do this:

```python
api_key = "sk-xxxxxxxx"
```

Use environment variables instead:

```python
api_key = os.getenv("OPENAI_API_KEY")
```

And add `.env` to `.gitignore`.

---

# 🚀 Future Architecture

The simple two-agent application can evolve into a production-style Agentic AI architecture:

```text
                         USER
                           |
                           v
                    Input Guardrails
                           |
                           v
                   +---------------+
                   | AutoGen Team  |
                   +-------+-------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Research       Developer      Reviewer
          Agent          Agent          Agent
             |             |             |
             +-------------+-------------+
                           |
                           v
                      RAG / Tools
                           |
                           v
                    Output Guardrails
                           |
                           v
                    Evaluation Layer
                           |
                           v
                     FINAL ANSWER
```

This provides a foundation for building more advanced **Agentic AI applications using Python and AutoGen**.

---

# ⭐ Key Takeaway

The main concept of this project is simple:

> **One agent performs the task, another agent reviews the work, and the team produces an improved response.**

This demonstrates the fundamental idea behind **Multi-Agent AI systems**.

---

# 👨‍💻 Author

**Dinesh Kumar**

AI & Java Full Stack Developer | GenAI | Agentic AI | Spring Boot | Python

🔗 LinkedIn:
[www.linkedin.com/in/dinesh-ai-man](http://www.linkedin.com/in/dinesh-ai-man)

---

# ⭐ If You Find This Useful

If this project helps you understand **AutoGen and Multi-Agent AI**, consider giving the repository a ⭐.

Follow me on LinkedIn for more content around:

* Generative AI
* Agentic AI
* RAG
* LangChain
* AutoGen
* CrewAI
* Python
* Java
* Spring Boot
* AI Engineering

---

## 📌 Project Roadmap

```text
✅ OpenAI Model Integration
        ↓
✅ Research Agent
        ↓
✅ Reviewer Agent
        ↓
✅ AutoGen Team
        ↓
⬜ Tool Calling
        ↓
⬜ RAG Integration
        ↓
⬜ Knowledge Graph
        ↓
⬜ Guardrails
        ↓
⬜ Evaluation
        ↓
⬜ Streamlit UI
        ↓
⬜ Production Agentic AI Application
```

---

## 📄 License

This project is intended for learning and demonstration purposes.
