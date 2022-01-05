def count_batteries_by_usage(cycles):
  lowCount=0, mediumCount=0, highCount=0
  arr=[100, 300, 500, 600, 900, 1000]
  for i in arr:
    if i<400:
      lowCount+=1
    elif 400<=i<919:
      mediumCount+=1
    else:
      highCount+=1
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  
arr=[100, 300, 500, 600, 900, 1000]      
count_batteries_by_usage(arr)      
print(lowCount, mediumCount,highCount)      


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
