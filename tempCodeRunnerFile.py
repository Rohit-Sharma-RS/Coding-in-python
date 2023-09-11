student_scores={"Harry":81,"Ron":78,"Hermione":99,"Draco":74,"Neville":62}
student_grades={}
for i in student_scores:
  if(student_scores[i]>=91):
    student_grades[i]="Outstanding"
  elif(student_scores[i]>=81):
    student_grades[i]="Exceeds Expectation"
  elif(student_scores[i]>=71):
    student_grades[i]="Acceptable"
  else:
    student_grades[i]="Fail"
print(student_grades)
