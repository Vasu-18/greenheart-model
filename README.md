# GreenHeart AI 🌱

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://greenheart.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**AI-powered agricultural assistant leveraging Gemini API for intelligent crop management**

![Plant Disease Analyzer Demo](assets/disease_demo.png) <!-- Update path -->
![Crop Recommendation Demo](assets/crop_demo.png) <!-- Update path -->

## ✨ Features

### 1. Plant Disease Analyzer 🔍
- Image-based plant health assessment
- Real-time analysis using Gemini Vision API
- Detailed disease identification and prevention advice
- Support for multiple crop varieties

### 2. Crop Recommendation System 🌾
- Climate-aware crop suggestions
- Soil parameter analysis (N-P-K, pH, moisture)
- Sustainable farming recommendations
- Market insights and yield optimization

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google API Key (for Gemini)

### Installation
```bash
# Clone repository
git clone https://github.com/Vasu-bansal-24/GreenHeart.git
cd GreenHeart

# Install dependencies
pip install -r requirements.txt
```

### Configuration
1. Create `.env` file in root directory:
```env
GOOGLE_API_KEY=your_api_key_here
```

### Run Application
```bash
streamlit run app.py
```

## 🛠️ Tech Stack

**Core Technologies**  
![Python](https://img.shields.io/badge/Python-3776AB?logo=python)
![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?logo=google)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit)

**Supporting Libraries**  
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn)

## 🌐 Live Demo

Access the production deployment:  
[https://greenheart.streamlit.app/](https://greenheart.streamlit.app/)

## � How It Works

```mermaid
graph TD
    A[User Input] --> B{Gemini API}
    B -->|Image Analysis| C[Disease Detection]
    B -->|Data Processing| D[Crop Recommendation]
    C --> E[Prevention Strategies]
    D --> F[Optimization Tips]
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 📧 Contact

**Vasu Bansal**  
[![Email](https://img.shields.io/badge/Email-vasu.bansal1204%40gmail.com-blue?logo=gmail)](mailto:vasu.bansal1204@gmail.com)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/vasu-bansal-45770228b/)