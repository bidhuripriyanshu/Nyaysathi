
# 🏛️ NyaySaathi: AI-Powered Legal Document Assistant
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![React](https://img.shields.io/badge/React-18.2.0-blue.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com/)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini-orange.svg)](https://ai.google.dev/)

> **Democratizing Legal Document Understanding with Dual AI Technology**

NyaySaathi is an intelligent web application that makes complex legal documents accessible to everyone. Using a hybrid AI approach with local processing (Ollama) and cloud enhancement (Google AI), it provides contract summarization, risk analysis, clause simplification, and multilingual translation.

![NyaySaathi Demo](https://nyaysathi-tawny.vercel.app)

> *Democratizing Legal Document Understanding with Dual AI Technology*

NyaySaathi is an intelligent web application that makes complex legal documents accessible to everyone. Using a hybrid AI approach with local processing (Ollama) and cloud enhancement (Google AI), it provides contract summarization, risk analysis, clause simplification, and multilingual translation.





## ✨ Key Features


### 📄 **Document Processing**
- **Multi-format Upload**: PDF, DOCX, TXT with drag-and-drop interface
- **Smart Text Extraction**: Automatic parsing and section detection
- **Risk Keyword Detection**: Highlights dangerous terms automatically

### 🤖 **Dual AI Analysis**
- **Local AI (Ollama)**: Privacy-first processing with Llama 3.2
- **Google AI (Gemini)**: Cloud-powered enhancement and risk analysis
- **Hybrid Intelligence**: Best of both privacy and accuracy

### 🧠 **Smart Features**
- **5-Point Summaries**: Contract overviews in plain language
- **Risk Analysis**: Professional-grade legal risk assessment
- **Clause Simplification**: Complex legal jargon to simple terms
- **Interactive Q&A**: Ask questions about your documents
- **Hindi Translation**: Multilingual accessibility for Indian users

### 🎨 **Modern Interface**
- **Professional Design**: Dark theme with smooth animations
- **Responsive Layout**: Works on desktop and mobile
- **Real-time Status**: Connection monitoring and feedback
- **Card-based UI**: Intuitive organization and navigation



## 🚀 Getting Started

### Prerequisites
- [Node.js 18+](https://nodejs.org/en/)
- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/) (for local AI)
- Google AI Studio API key (for cloud AI)

### Quick Installation


1. **Clone the repository**
cd Nyaysathi

text

2. **Setup Backend**
cd backend
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt

text

3. **Setup Frontend**
cd ../frontend
npm install

text

4. **Configure AI Services**

4. *Configure AI Services*
Install and setup Ollama
Terminal 1: Start backend
cd backend
uvicorn app:app --reload --port 8000

Terminal 2: Start frontend
cd frontend
npm run dev

text

Open [http://localhost:5173](http://localhost:5173) to access NyaySaathi!

---

## 💡 Usage Examples

### Basic Workflow
1. **Upload** your legal document (contract, agreement, etc.)
2. **Generate Summary** using local AI for privacy
3. **Enhance** with Google AI for professional insights
4. **Analyze Risks** to identify potential legal issues
5. **Translate** to Hindi for broader accessibility
6. **Ask Questions** about specific clauses or terms

### Sample Use Cases
- **Small Business**: Understanding supplier contracts
- **Freelancers**: Analyzing service agreements and NDAs
- **Students**: Learning legal document structure
- **Rural Communities**: Accessing legal help in local languages



## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** for fast development
- **Framer Motion** for animations
- **Lucide React** for icons

### Backend
- **FastAPI** with Python
- **Ollama** for local LLM processing
- **Google AI Studio** for cloud enhancement
- **pypdf & python-docx** for document parsing

### AI Models
- **Llama 3.2** (local processing)
- **Google Gemini 1.5 Flash** (cloud enhancement)
<<<<<<< HEAD

1. *Upload* your legal document (contract, agreement, etc.)
2. *Generate Summary* using local AI for privacy
3. *Enhance* with Google AI for professional insights
4. *Analyze Risks* to identify potential legal issues
5. *Translate* to Hindi for broader accessibility
6. *Ask Questions* about specific clauses or terms

### Sample Use Cases
- *Small Business*: Understanding supplier contracts
- *Freelancers*: Analyzing service agreements and NDAs
- *Students*: Learning legal document structure
- *Rural Communities*: Accessing legal help in local languages


## 🛠 Tech Stack

### Frontend
- *React 18* with TypeScript
- *Vite* for fast development
- *Framer Motion* for animations
- *Lucide React* for icons

### Backend
- *FastAPI* with Python
- *Ollama* for local LLM processing
- *Google AI Studio* for cloud enhancement
- *pypdf & python-docx* for document parsing

### AI Models
- *Llama 3.2* (local processing)
- *Google Gemini 1.5 Flash* (cloud enhancement)

---

## 📁 Project Structure

Nyaysathi/
├── backend/
│   ├── app.py              # FastAPI main application
│   ├── gemini_client.py    # Google AI integration
│   ├── extract.py          # Document processing
│   ├── prompts.py          # AI prompt templates
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.tsx         # Main application
│   │   └── api.ts          # Backend communication
│   ├── package.json        # Node dependencies
│   └── index.html          # Entry point
└── README.md




---



### Environment Variables
Create `backend/.env`:
GEMINI_API_KEY=your-google-ai-studio-key
OLLAMA_URL=http://localhost:11434



### Customization
- **Models**: Change AI models in `gemini_client.py` and via Ollama
- **Prompts**: Modify templates in `prompts.py`
- **Styling**: Update themes in `frontend/src/index.css`
- **Languages**: Add translations in `gemini_client.py`

- *Models*: Change AI models in gemini_client.py and via Ollama
- *Prompts*: Modify templates in prompts.py
- *Styling*: Update themes in frontend/src/index.css
- *Languages*: Add translations in gemini_client.py
---

## 🎯 Roadmap


- [ ] **Document Comparison**: Side-by-side contract analysis
- [ ] **Template Library**: Pre-built legal document templates
- [ ] **Advanced Analytics**: Document compliance scoring
- [ ] **Multi-language**: Support for more Indian languages
- [ ] **API Integration**: Third-party legal service connectors
- [ ] **Mobile App**: React Native version

- [ ] *Document Comparison*: Side-by-side contract analysis
- [ ] *Template Library*: Pre-built legal document templates
- [ ] *Advanced Analytics*: Document compliance scoring
- [ ] *Multi-language*: Support for more Indian languages
- [ ] *API Integration*: Third-party legal service connectors
- [ ] *Mobile App*: React Native version



## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

1. *Fork* the repository
2. *Create* a feature branch (git checkout -b feature/AmazingFeature)
3. *Commit* changes (git commit -m 'Add some AmazingFeature')
4. *Push* to branch (git push origin feature/AmazingFeature)
5. *Open* a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.



## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## 👥 Team

Created by **NigHtMare16K** and contributors

- 🐛 **Bug Reports**: [Create an Issue](https://github.com/NigHtMare16K/Nyaysathi/issues)
- 💡 **Feature Requests**: [Discussions](https://github.com/NigHtMare16K/Nyaysathi/discussions)
- 📧 **Contact**: [GitHub Profile](https://github.com/NigHtMare16K)
Created by *NigHtMare16K* and contributors

- 🐛 *Bug Reports*: [Create an Issue](https://github.com/NigHtMare16K/Nyaysathi/issues)
- 💡 *Feature Requests*: [Discussions](https://github.com/NigHtMare16K/Nyaysathi/discussions)
- 📧 *Contact*: [GitHub Profile](https://github.com/NigHtMare16K)



## 🙏 Acknowledgments

- **Google AI Studio** for free AI API access
- **Ollama** for local LLM infrastructure  
- **React & FastAPI** communities for excellent frameworks
- **Open Source Contributors** who make projects like this possible

- *Google AI Studio* for free AI API access
- *Ollama* for local LLM infrastructure  
- *React & FastAPI* communities for excellent frameworks
- *Open Source Contributors* who make projects like this possible


## ⭐ Star History

If NyaySaathi helps you understand legal documents better, please consider giving it a star! ⭐



<div align="center">

**Made with ❤️ for accessible legal technology**


