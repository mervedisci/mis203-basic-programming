while True:
  student_name = input("Enter Student Name: ")
  score = int(input("Enter Score: "))
  if score < 0 or score > 100:
    print("Invalid Score. Please Enter A Number Between 0 And 100")
    continue
  elif score >= 90 and score <= 100:
    letter = "A"
  elif score >= 80 and score < 90:
    letter = "B"
  elif score >= 70 and score < 80:
    letter = "C"
  elif score >= 60 and score < 70:
    letter = "D"
  elif score < 60:
    letter = "F"
  print(f"{student_name}'s score is {score} -> {letter}")
  if student_name == "q":
    break
