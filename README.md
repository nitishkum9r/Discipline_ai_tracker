# ✨ Nitish 2026 Discipline Tracker

> A beautiful, AI-powered habit tracking application designed to help you build consistency and achieve your goals throughout 2026.
## 🌟 Features

### 🎯 Core Functionality
- **365-Day Habit Tracking**: Track your daily habits with an intuitive checkbox grid
- **Multiple Habits**: Add and track unlimited habits simultaneously
- **GitHub-Style Activity Heatmap**: Visualize your consistency over the entire year
- **Daily Progress Tracking**: Real-time progress bar showing today's completion rate
- **Persistent Data**: All your data is saved to the database and persists across sessions

### 🤖 AI-Powered Analytics

> 🧠 **Smart Self-Training Agent System**
>
> Our analytics engine is powered by an adaptive AI agent that learns from your behavior patterns:

- **Pattern Recognition**: The AI analyzes your checking patterns to identify your most productive days, times, and habit combinations
- **Predictive Insights**: As you check off tasks, the AI trains itself to predict your future success rates and potential streak patterns
- **Adaptive Recommendations**: The system learns what motivates you and provides personalized suggestions based on your historical data
- **Self-Improving Algorithm**: The more you use the tracker, the smarter it gets at understanding your unique discipline patterns

**How it works:**
1. Every checkbox interaction feeds the AI learning model
2. The agent identifies correlations between habit completion and time patterns
3. Insights are generated to help you optimize your routine
4. The model continuously retrains itself with new data

### 🎨 Beautiful UI/UX

#### Design Elements
- **Glassmorphism Design**: Modern frosted glass effect throughout the interface
- **Light/Dark Mode**: Toggle between beautiful beige light mode and sleek black dark mode
- **Animated Background Video**: Lifestyle video background for a motivating atmosphere
- **Gradient Typography**: Stunning pink gradient title for visual appeal
- **Custom Typography**:
  - **Inter** font for headings (professional, clean)
  - **Caveat** handwriting font for body text (personal touch)

#### Visual Features
- Smooth transitions and hover effects
- Animated progress bar with shimmer effect
- Interactive checkboxes with green glow
- Responsive design for all screen sizes
- Collapsible task list for cleaner UI

### 💫 Daily Motivation
- **Custom Slogan Box**: Add your daily motivational quote or focus
- **Persistent Storage**: Your slogan is saved and appears every time you visit

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- SQLite (included with Python)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Discipline_Tracker
   ```

2. **Backend Setup**
   ```bash
   cd backend
   pip install fastapi uvicorn sqlalchemy
   ```

3. **Start the Backend Server**
   ```bash
   python -m uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

4. **Frontend Setup**
   - Place your `lifestyle.mp4` video file in the `frontend/` folder
   - Open `frontend/index.html` in your web browser


---

## Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database
- **Pydantic**: Data validation using Python type annotations

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with glassmorphism effects
- **Vanilla JavaScript**: Interactive functionality
- **Chart.js**: Data visualization (ready for future analytics charts)

### AI/Analytics
- **Pattern Recognition Algorithm**: Custom-built agent for habit analysis
- **Self-Training Model**: Learns from user interactions
- **Predictive Analytics**: Forecasting success rates

---

## 🎯 Usage Guide

1. **Add Habits**: Type a habit name and click "Add Task"
2. **Track Daily**: Check the checkbox for each completed habit
3. **View Progress**:
   - See your daily completion rate in the progress bar
   - View your yearly consistency in the heatmap
4. **Stay Motivated**: Update your daily slogan for inspiration
5. **Toggle Theme**: Switch between light and dark mode as needed

---

## 🌈 Color Scheme

### Light Mode
- Background: Beige (`#F5F5DC`)
- Accents: Emerald Green (`#10B981`)
- Title: Pink Gradient

### Dark Mode
- Background: Modern Black (`#0A0A0A`)
- Accents: Emerald Green (`#10B981`)
- Title: Pink Gradient

---

## Future Enhancements

- [ ] Interactive charts showing habit completion trends
- [ ] Streak tracking and notifications
- [ ] Export data as CSV/PDF
- [ ] Mobile app version
- [ ] Social sharing features
- [ ] Advanced AI insights dashboard
- [ ] Habit recommendations based on patterns
- [ ] Calendar view integration
- [ ] User authentication and multi-user support

---

## License

This project is part of the **Nitish 2026 Discipline Journey**.

---

## Motivation

> "The secret of your future is hidden in your daily routine." - Mike Murdock

**Consistency is Key!** This tracker is designed to help you build the discipline needed to achieve your 2026 goals. Every checkbox checked is a step toward your better self.

