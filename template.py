from calculatetimings import calculateKeyHoldTime
import json
import statistics

def extractKeyHoldTime(text, user):
	all_keyHoldTime = []
	
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
	
	for timings in data:
		kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
		all_keyHoldTime.append(kht)
	
	return all_keyHoldTime

def generateComparatorFAR(text, user):
	all_kht = extractKeyHoldTime(text, user)
	mn = [statistics.mean(list(lst)) for lst in zip(*all_kht)]
	st = [statistics.stdev(list(lst)) for lst in zip(*all_kht)]
	comp = [(m - s, m + s) for m, s in zip(mn, st)]
	return comp

def generateComparatorFRR(text, user):
	all_kht = extractKeyHoldTime(text, user)[:20]
	mn = [statistics.mean(list(lst)) for lst in zip(*all_kht)]
	st = [statistics.stdev(list(lst)) for lst in zip(*all_kht)]
	comp = [(m - s, m + s) for m, s in zip(mn, st)]
	return comp