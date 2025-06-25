# SDG Project Idea Generator API 🌍

This project provides a web application and API for generating sustainable project ideas based on UN Sustainable Development Goals (SDGs) and evaluating problem statements. The system uses Gemini AI to generate creative and feasible project ideas for students.

## Features

- Select up to 2 SDGs to generate project ideas
- Generate student-friendly, realistic project ideas
- Evaluate problem statements based on comprehensive criteria
- Interactive web interface using Streamlit
- FastAPI backend for efficient request handling

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Model**: Google's Gemini-1.5-flash
- **Additional Libraries**: 
  - google-generativeai
  - python-dotenv
  - pydantic
  - uvicorn

## Project Structure

```
├── app.py              # Streamlit frontend application
├── main.py            # FastAPI backend server
├── marking_ps_gemini.py # Problem statement evaluation logic
├── requirements.txt    # Project dependencies
└── streamlit_and_fast.py # Combined Streamlit and FastAPI implementation
```

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Running the Application

1. Start the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
2. Start the Streamlit frontend:
   ```bash
   streamlit run app.py
   ```

## API Endpoints

### 1. Generate Ideas
- **Endpoint**: `/generate_ideas`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "sdgs_selected": ["SDG1", "SDG2"]
  }
  ```

### 2. Evaluate Problem Statement
- **Endpoint**: `/evaluate_ps`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "idea": "Project idea",
    "problem_statement": "Problem statement text"
  }
  ```

## Problem Statement Evaluation Criteria

The system evaluates problem statements based on 10 key criteria:
1. Contains Data
2. References Included
3. Location/Area Clear
4. Target Audience Clearly Stated
5. Impact Described
6. Grammar
7. Demonstrates Understanding
8. Precise and To the Point
9. Relevant to the Idea
10. Well-structured and Easy to Understand

## Supported SDGs

The application supports all 17 UN Sustainable Development Goals:
- No Poverty
- Zero Hunger
- Good Health and Well-being
- Quality Education
- Gender Equality
- Clean Water and Sanitation
- Affordable and Clean Energy
- Decent Work and Economic Growth
- Industry, Innovation and Infrastructure
- Reduced Inequalities
- Sustainable Cities and Communities
- Responsible Consumption and Production
- Climate Action
- Life Below Water
- Life on Land
- Peace, Justice and Strong Institutions
- Partnerships for the Goals

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License.
