def count_batteries_by_usage(cycles):
    dict = {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  for charge_cycles in cycles:
        if charge_cycles < 0:
            raise Exception("Value cannot be negative")
        if charge_cycles > 910:
            dict['highCount']+=1
        elif charge_cycles >= 410:
            dict['mediumCount']+=1
        elif charge_cycles >=0:
            dict['lowCount']+=1

  return dict
  


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
