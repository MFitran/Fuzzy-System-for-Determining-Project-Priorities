# Fuzzy System for Determining Project Priorities Based on Budget, Duration, and Impact on Business

## Description
This project aims to develop a project prioritization system using fuzzy logic, which can help companies select and prioritize projects more effectively amidst information uncertainty. In a competitive business environment, sound decisions are critical to a company's success.

## Main Components
1. **Fuzzification:** Uses three input parameters (budget, duration, and business impact) to determine a project's priority value.
2. **Inference Rule:** Apply inference rules to relate input parameters to project priority outputs.
3. **Defuzzification:** Uses the Mamdani method to produce crisp values ​​from fuzzy output, providing results that are intuitive and easy to understand.
Results: This project shows how fuzzy systems can provide more adaptive and flexible solutions in project decision making, as well as increasing the efficiency of project management in companies.

## Technology Used
1. Python (numpy, matplotlib)
2. Fuzzy logic method

## How to Run
1. Clone this repository to your computer.
2. Make sure you have Python installed on your system.
3. Install the required libraries: numpy and matplotlib
4. When the code is run, the following outputs will be displayed:
    1. System Introduction: A brief explanation of the purpose of the fuzzy system.
    2. Input Criteria: Prompts the user to enter values for the following criteria.
        1. Budget
        2. Duration
        3. Business Impact
    3. Evaluation Process: Displays a message indicating that the system is calculating priorities.
    4. Priority Output: Shows the calculated project priority, for example:
        "Project Priority: High"
    5. Criteria Details: Explains how each criterion contributes to the final priority.
