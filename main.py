
def count_batteries_by_usage(cycles):
  def count_batteries_by_usage(cycles):
    lowCount = " "
    highCount=""
    mediumCount =""
    for i in range (len(cycles)):
        if cycles[i]<410:
            lowCount+=str(cycles[i])
        elif cycles[i]>410 and cycles[i]<909:
            mediumCount +=str(cycles[i])
        else:
            highCount+=str(cycles[i])


  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
