with open('QUESTION.TXT', 'r', encoding="utf8") as f:  
    lines = f.readlines()  
  
odd_lines = [line.replace("\n","") for i, line in enumerate(lines) if i % 2 == 0]
print(odd_lines)