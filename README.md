Perfect 👍 Here’s the **entire `README.md`** file in copy-paste ready format.

````markdown
# COMP163 Assignment 3 – Semester Success Simulator  

About the Game  
This is a **text-based simulation game** where the player takes on the role of a student trying to balance school and life.  
The player makes choices about:  
- Course load (Light, Standard, Heavy)  
- Study strategies (Programming, Math, English, History)  
- Final semester decisions  

Each choice affects the player’s **GPA, study hours, social points, and stress level**, leading to different possible outcomes.  

---

 Branching Concepts Demonstrated  

- Step 1: Foundation Setup 
  Variables `student_name`, `current_gpa`, `study_hours`, `social_points`, and `stress_level` are initialized.  

- Step 2: Course Planning Decision  
  Uses **if/elif/else** and **comparison operators (>=, <=, ==, !=)** to adjust `study_hours` and `stress_level` based on GPA and course load.  

- Step 3: Study Strategy Decision
  Uses **membership operators (`in`, `not in`)** to validate study choice from:  
  ```python
  ["Programming", "Math", "English", "History"]
````

Uses logical operators (`and`, `or`, `not`) to update GPA and social points based on strategy.

Step 4: Final Semester Assessment**
  Combines all concepts:

   Identity operators (`is`, `is not`)** for type checking
   Nested if statements** (minimum 2 levels) to generate outcomes
   3+ endings based on final stats

---

 How to Run the Game

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/comp163-assignment-3.git
   cd comp163-assignment-3
   ```

2. Run the program:

   ```bash
   python3 yourusername_assignment_3.py
   ```

---

Possible Endings

 Ending 1: Academic Excellence
  GPA is high (≥ 3.5), stress is managed, and study hours are effective.

 Ending 2: Burnout
  Study hours are very high, but stress ≥ 80 causes failure despite effort.

 Ending 3: Party Lifestyle
  Social points are high, but GPA ≤ 2.0 results in academic probation.

 Ending 4: Balanced Success
  Stats are moderate across GPA, study hours, social points, and stress, leading to a happy, balanced semester.

---

Final Statistics

At the end of the game, the following stats are displayed to reflect the player’s decisions:

* GPA
* Study Hours
* Social Points
* Stress Level

AI Assistance

Parts of this project were developed with assistance from AI, specifically for:

* Debugging code errors
* Explaining GitHub workflows (repository, commits, pushes)
* Code review


