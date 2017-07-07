from calculatetimings import calculateKeyHoldTime
import json

def authenticateFAR(text, user, comp):
	FAR = 0.0
	total = 0.0
	
	usr = [u for u in range(1, 12) if not u == user]
	for user in usr:
		filename = 'processedData/text{0}/user{1}.json'.format(text, user)
		with open(filename, 'r') as f:
			data = [json.loads(line) for line in f]
		
		for timings in data:
			flag = 'g'
			kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
			imp = 0.0
		
			for k in zip(kht, comp):
				if k[0] > k[1][0] and k[0] < k[1][1]:
					flag = 'f'
					imp += 1.0

			if flag == 'f' and imp >= 0.8*len(kht):
				FAR += 1.0
			total += 1.0

	return (FAR/total)*100.0

def authenticateFRR(text, user, comp):
	FRR = 0.0
	total = 0.0
	
	filename = 'processedData/text{0}/user{1}.json'.format(text, user)
	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f]
		
	for timings in data[20:]:
		flag = 'g'
		kht = calculateKeyHoldTime(timings['keyPressData'], timings['keyReleaseData'])
		imp = 0.0
	
		for k in zip(kht, comp):
			# sign reversed for FRR; and logical operator changed to 'or'
			if k[0] < k[1][0] or k[0] > k[1][1]:
				flag = 'f'
				imp += 1.0

		if flag == 'f' and imp >= 0.6*len(kht):
			FRR += 1.0
		total += 1.0

	return (FRR/total)*100.0