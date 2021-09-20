from collections import defaultdict

def longestEqualSequence(sequence):
  sequence_dict = defaultdict(int)
  longest_sequence = 0
  current_count = 1
  currest_sequence_list = []
  longest_sequence_list = []
  previous_counter = 0
  for i  in range(len(sequence)):
    # If the input list is only one element, the longest sequence will be that input list
    if len(sequence) == 1:
      longest_sequence_list = sequence
    if i > 0:
      # If this is an equal sequence, i.e) [..., 6, 6, ...] previous = 6 and sequence[i] = 6
      if previous_number == sequence[i]:
        # Increment the current count of the current sequence by one. 
        # current_count = current_count + 1
        current_count += 1
        # If the element is the last element of the list,
        # check if the current sequence is the longest equal sequence
        # if it is, assign the current sequence to the longest_sequence_list
        if i == len(sequence) - 1:
          if longest_sequence < current_count:
            longest_sequence = current_count
            longest_sequence_list = currest_sequence_list
      # If this not an equal sequence, i.e)  [..., 1, 6, ...] previous = 1 and sequence[i] = 6
      else: 
        # Check if the current longest sequence is the longest equal sequence 
        # if it is, assing the current sequence to the longest_sequence_list
        if longest_sequence < current_count:
          longest_sequence = current_count
          longest_sequence_list = currest_sequence_list
        # After checking if the current list is the longest equal sequence,
        # clear the current equal sequence list
        currest_sequence_list = []
        current_count = 1
    # After each loop, assign the current value to the previous number
    previous_number = sequence[i]
    currest_sequence_list.append(sequence[i])
    
  return longest_sequence_list

a = [int(x) for x in input("Enter a list of numbers with space in between each number:").split()]
print("Longest Sequence of the list", a, "is")
print(longestEqualSequence(a))
