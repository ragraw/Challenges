

def test(message_file):
  # get map of int : string and list of number inputs
    map = {}
    nums = []
    with open(message_file) as f:
        for line in f:
            (key, val) = line.split()
            map[int(key)] = val
            nums.append(int(key))
    # Read the pyramid
    nums.sort()
    read_index = 0
    nums_read = 1
    final = ""
    while read_index < len(nums):
        final = final + " " + map[nums[read_index]] 
        nums_read = nums_read + 1
        read_index = read_index + nums_read
    print("final = " + final)
    return final

test("input2.txt")
 