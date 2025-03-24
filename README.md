# 🚀 Multi-Agent SEO Blog Generator

This project is a **multi-agent system** that automatically generates **SEO-optimized blog posts** on trending HR topics. It utilizes multiple AI agents to research, plan, generate, optimize, and review content.

## 📖 Features
✅ **Automated Research** – Finds trending HR topics  
✅ **Content Planning** – Generates a structured outline  
✅ **AI-Powered Writing** – Creates comprehensive blog content  
✅ **SEO Optimization** – Ensures high-ranking keywords and meta descriptions  
✅ **Proofreading & Review** – Improves readability and correctness  

---

## 🏗️ **System Architecture**
The project follows a modular architecture with multiple AI agents:

1️⃣ **Research Agent** – Fetches trending HR topics from the web.  
2️⃣ **Content Planning Agent** – Creates an article outline based on the selected topic.  
3️⃣ **Content Generation Agent** – Writes the blog post using AI.  
4️⃣ **SEO Optimization Agent** – Optimizes content for search engines.  
5️⃣ **Review Agent** – Proofreads and enhances content quality.  

### **Workflow**
```mermaid
graph TD;
    A[Research Agent] --> B[Content Planner];
    B --> C[Content Generator];
    C --> D[SEO Optimizer];
    D --> E[Review Agent];
    E --> F[Final Blog];
