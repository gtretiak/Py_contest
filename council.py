import sys # to read from STDIN
from collections import defaultdict # to initialize default values (zero, empty list, etc)

def main():
    print("=== Reliable Annotation Aggregator ===")
    print("This program filters reliable workers and aggregates their task responses.")
    print("Expected input format (from stdin or file):")
    print("1. First block: gold standard task verdicts (format: task_id verdict)")
    print("2. Second block: worker responses (format: worker_id task_id verdict)")
    print("Example:")
    print("  A1 1")
    print("  A2 0")
    print("  A3 1")
    print("  [then worker responses like:]")
    print("  W1 A1 1")
    print("  W1 A3 0")
    print("  W2 A2 0")
    print("Then if you use STDIN press CTRL+D")
    print("=======================================\n")
    # Reading the input, line by line, splitting space-separated strings
    lines = [line.strip() for line in sys.stdin if line.strip()]
    tasks_with_known_answers = {} # tasks with known answer to evaluate other responses
    responses = []
    # storing the known answers
    i = 0
    while i < len(lines): # iterating through all the given lines 
        parts = lines[i].split() # we split them, and if there are just two strings..,
        if len(parts) == 2: #... that means we look at the tasks with known answers
            task_id, verdict = parts
            tasks_with_known_answers[task_id] = int(verdict) # we assign the value to the task
            i += 1 # and proceed
        else:
            break # we came across other responses to evaluate...
    # stroing others' answers
    worker_lines = lines[i:] # fetch all the lines, starting from the iterated index i 
    worker_data = []
    for line in worker_lines:
        parts = line.split()
        if len(parts) == 3: 
            worker_id, task_id, verdict = parts
            worker_data.append((worker_id, task_id, int(verdict))) # we store the worker_ids, tasks, and their answers
    # Now it's time to evaluate the answers and workers' accuracy 
    worker_accuracy = defaultdict(lambda: [0, 0]) # creating a dictionary with workers, correct and total answers
	# we use lambda (quick, small, unnamed function) to set all predefined as zeros
    for worker_id, task_id, verdict in worker_data: # for each entity in worker_data
        if task_id in tasks_with_known_answers: # if this is the question (task) we know the right answer for
            correct_verdict = tasks_with_known_answers[task_id]
            worker_accuracy[worker_id][1] += 1 # here we store total number of answer to calculate accuracy
            if verdict == correct_verdict: # if it's match with the right one
                worker_accuracy[worker_id][0] += 1 # we increase the number of correct answers
    # Then we decide on where's the threashold (accuracy >= 0.6 or might be different)
    good_workers = set() # Empty set creation to store workers who are good enough
    for worker_id in worker_accuracy:
        correct, total = worker_accuracy[worker_id]
        if total > 0 and correct / total >= 0.6: # if at least one answer is given and >= 60% of them are correct
            good_workers.add(worker_id) # we designate the worker as a good boy
    # Then we collect all the answers to the rest questions (tasks) from the good workers
    task_answers = defaultdict(list) # a dictionary creation
    for worker_id, task_id, verdict in worker_data:
        if task_id not in tasks_with_known_answers and worker_id in good_workers: # if the answer isn't known AND...
            task_answers[task_id].append(verdict) #... this is the good boy we fetch their answers to the list
    # Now it's time to hear the majority...
    result = {} # initializing an empty dictionary to store final verdicts
    for task_id in task_answers: # for every task that has an answer from good workers
        answers = task_answers[task_id] # store answers
        if not answers: # if the list is empty we skip it
            continue
        freq = defaultdict(int) # the dictionary creation to store the frequency of each uniq answer
        for ans in answers:
            freq[ans] += 1 # increasing the total number of the same answer appearance 
        if not freq:
            continue
        # Let's find the max frequent answer
        max_freq = max(freq.values())
        candidates = [ans for ans in freq if freq[ans] == max_freq] # list of answers with max frequency (might be more than one)
        chosen_ans = min(candidates) # here we choose the smallest, but it might be anything we need
        result[task_id] = chosen_ans # we save the answer
    # For every task we print it the sorted order
    for task_id in sorted(result.keys()):
        print(task_id, result[task_id])

if __name__ == "__main__":
    main()
