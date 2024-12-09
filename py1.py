import requests as r
class Fetcher:
  def __init__(self):
    l=r.get("https://cdn.ituring.ir/ex/users.json").json()
    self._student =l.json()

  def nerds(self):
    names = set()
    for student in self._students:
      if student['score']>18.5:
         name =student['name'] +" "+ student['last_name']
         names.add(name)
         return names

  def sultans(self):
    max_score = 0
    sultans = []
    for student in self._students:
      if student ['score']>max_score:
        max_score = student['score']
        sultans = student['name'] +" "+ student['last_name']   
      elif student['score'] ==max_score:
        sultans.append(student['name'] +" "+ student['last_name'])
    return tuple(sultans)

  def mean(self):
    total = 0
    count = len(self._students)
    for student in self._student:
      if count:
        return total/count
      else:
        return 0

  def get_students(self):
    cleaned_list=[]
    for student in self._students:
      filtered_student={
          'first_name':student['name'],'last_name':student['last_name'],'score':student['score'] }  
      cleaned_list.append(filtered_student)
      return cleaned_list    
D=Fetcher()
print(D.nerds())
print(D.sultans())
print(D.mean())
print(D.get_students())