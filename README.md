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
1. **Clone:** Clone this repository to your computer.
2. **Install Python:** Make sure you have Python 3.9 or above installed on your system.
3. **Install the required libraries:** numpy and matplotlib
5. **Set Your Input Values:** Locate the section of the code where the input values are defined. You will find the following lines (line 99 - 101):
   ``` python
   anggaran_input = 95
   durasi_input = 45
   pengaruh_input = 80
   ```
6. **View the Output:** The script will print the fuzzified values for budget, duration, and impact, as well as the inferred fuzzy output for project priority. It will also display a graph of the fuzzy output aggregation and print the defuzzified priority value.

