# Author: Eric Zhang ecz5032@psu.edu
#Collaborator: Ajith Obili ako5278@psu.edu
#Collaborator: Craig John cxj5287@psu.edu
#Collaborator: Sai pal sqp5889@psu.edu
#Section 5
#Breakout Room 2 

def getLetterGrade(grade):
  if grade >= 93.0:
    return "A"
  elif grade >= 90.0:
    return "A-"
  elif grade >= 87.0:
    return "B+"
  elif grade >= 83.0:
    return "B"
  elif grade >= 80.0:
    return "B-"
  elif grade >= 77.0:
    return "C+"
  elif grade >= 70.0:
    return "C"
  elif grade >= 60.0:
    return "D"
  else:
    return "F"

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

if __name__ == "__main__":
  run()
  