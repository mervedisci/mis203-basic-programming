count = 0
total = 0
while True:
  student_name = input("Enter Student Name('q' to quit: ")
  if student_name == "q":
    break
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
  
  count += 1
  total = total + score
if count == 0:
  print("No student entered.")
else: 
  average = total / count
  print(f"{count} student entered.")
  print(f"Average score: {average:2f}")
