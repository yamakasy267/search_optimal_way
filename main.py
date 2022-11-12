
import os

def search(matrix, first_line, sort_end_line):
  ret = []
  put=[]
  min_put = []
  point = 0
  count = 0
  distances  = min(filter(lambda val: val > 0, matrix[0][1:first_line[0]+1]))
  index = (matrix[0].index(distances))
  put.append(index)
  matrix[0][index] = 0
  count+=1
  while(distances+sum(min_put) < sort_end_line[p]):
    if (count>0 and count <25):
      point = min(filter(lambda val: val > 0, matrix[index][1:]))
      index = (matrix[index][1:].index(point))+1
      for deli in range(len(matrix)):
        matrix[deli][index] = 0
      distances += point
      put.append(index)
      if (index <= first_line[0]):
        count+=1
      else:
        count-=1
    else:
      if count == 0:
        point = min(filter(lambda val: val > 0, matrix[index][1:first_line[0]+1]))
        index = (matrix[index][1:first_line[0]+1].index(point))+1
        for deli in range(len(matrix)):
          matrix[deli][index] = 0
        distances += point
        put.append(index)
        count+=1
      else:
        point = min(filter(lambda val: val > 0, matrix[index][first_line[0]+1:]))
        index = (matrix[index][first_line[0]+1:].index(point))+first_line[0]+1
        for deli in range(len(matrix)):
          matrix[deli][index] = 0
        distances += point
        put.append(index)
        count-=1
    min_put.append(min(filter(lambda val: val > 0, matrix[index][1:first_line[0]+1])))
    teor_index = (matrix[index][1:first_line[0]+1].index(min_put[0]))+1
    for t in range(count):
      min_put.append(min(filter(lambda val: val > 0, matrix[teor_index][first_line[0]+1:])))
      teor_index = (matrix[teor_index][first_line[0]+1:].index(min_put[t+1]))+first_line[0]+1
  for t in range(count):
    point = min(filter(lambda val: val > 0, matrix[index][first_line[0]+1:]))
    index = (matrix[index][first_line[0]+1:].index(point))+first_line[0]+1
    for deli in range(len(matrix)):
      matrix[deli][index] = 0
    distances += point
    put.append(index)
  count=0
  put.insert(0,distances)
  return put

def Writer(output_file,all_put,end_line):
  with open(output_file ,'a') as f:
    for i in end_line:
      f.writelines("%s\t" % place for place in all_put[i])
      f.write("\n")


directory = 'test'
arr = []
matrix =[]
distances1 = []
all_put={}
for filename in os.listdir(directory):
  f = os.path.join(directory, filename)
  if os.path.isfile(f) and filename.endswith('.txt'):
    arr.append(f)
for i in arr:
  with open(i) as f:
    first_line = list(map(int,f.readline().split()))
    for j in f:
      matrix.append(list(map(int,j.split())))
  end_line = matrix.pop()
  sort_end_line = end_line
  sort_end_line.sort()
  for p in range(first_line[2]):
    put = search(matrix,first_line,sort_end_line)
    distances = put.pop(0)
    put.insert(0,len(put))
    distances1.append(put[0])
    all_put[p] = put
    if distances > end_line[p]:
      print("no", i,p,distances)
  output_file = i.replace("input","output").replace("test","tes1")
  Writer(output_file, all_put,end_line)
  break
print(sum(distances1)/2)
