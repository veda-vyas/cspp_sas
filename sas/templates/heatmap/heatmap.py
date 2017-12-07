import csv
import timestring
import pytz
import datetime

IST = pytz.timezone('Asia/Kolkata')
def heatmap(input,output):
	with open(input, 'rb') as csvfile:
		with open(output, 'wb') as csvfile2:
		    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		    submission_count = 0
		    critical_questions = {"MODULE1 ACTIVITY1":"1.1","MODULE1 ACTIVITY2":"2.1","MODULE1 ACTIVITY3":"3.1","MODULE1 ACTIVITY4":"4.1","MODULE1 ACTIVITY5":"5.2","MODULE1 ACTIVITY6":"6.1","MODULE1 ACTIVITY7":"7.2","MODULE1 ACTIVITY8":"8.1","MODULE1 ACTIVITY9":"9.1"}
		    activity_codes = {"MODULE1 ACTIVITY1 SUBMISSION":"1","MODULE1 ACTIVITY2 SUBMISSION":"2","MODULE1 ACTIVITY3 SUBMISSION":"3","MODULE1 ACTIVITY4 SUBMISSION":"4","MODULE1 ACTIVITY5 SUBMISSION":"5","MODULE1 ACTIVITY6 SUBMISSION":"6","MODULE1 ACTIVITY7 SUBMISSION":"7","MODULE1 ACTIVITY8 FILE SUBMISSION":"8","MODULE1 ACTIVITY8 SUBMISSION":"8","MODULE1 ACTIVITY9 FILE SUBMISSION":"9"}
		    submissions = {}
		    hours = [9,10,11,12,13,14,15,16,17,18]
		    for row in csvreader:
		        if "SUBMISSION" in row[2] and "DOWNLOADED" not in row[2] and row[3] != '':
		        	if critical_questions[row[2].split(' ')[0]+' '+row[2].split(' ')[1]] == row[3].split(' ')[0]:
						submission_count+=1
						csvwriter = csv.writer(csvfile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						localized_datetime = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=pytz.utc).astimezone(IST)
						hour = timestring.Date(localized_datetime).hour
						if hour in hours:
							if (activity_codes[row[2]],hour) in submissions:
								submissions[(activity_codes[row[2]],hour)] += 1
							else:
								submissions[(activity_codes[row[2]],hour)] = 1
						else:
							if (activity_codes[row[2]],'*') in submissions:
								submissions[(activity_codes[row[2]],'*')] += 1
							else:
								submissions[(activity_codes[row[2]],'*')] = 0
		    sorted_submissions = sorted(submissions, key=lambda element: (element[0], element[1]))
		    current_activity = ""
		    current_value = 0
		    for entry in sorted_submissions:
		    	if entry[0] ==  current_activity:
			    	csvwriter.writerow([entry[0],entry[1],int(submissions[entry])])
		    return sorted_submissions

print heatmap('SAS-03-10-17.csv','heatmap.csv')

# import csv
# with open('SAS-03-10-17.csv', 'rb') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     submission_count = 0
#     critical_questions = {"MODULE1 ACTIVITY1":"1.1","MODULE1 ACTIVITY2":"2.1","MODULE1 ACTIVITY3":"3.1","MODULE1 ACTIVITY4":"4.1","MODULE1 ACTIVITY5":"5.2","MODULE1 ACTIVITY6":"6.1","MODULE1 ACTIVITY7":"7.2","MODULE1 ACTIVITY8":"8.1","MODULE1 ACTIVITY9":"9.1"}
#     submission_emails = {}
#     for row in csvreader:
#         if "SUBMISSION" in row[2] and "DOWNLOADED" not in row[2] and row[3] != '':
#         	if critical_questions[row[2].split(' ')[0]+' '+row[2].split(' ')[1]] == row[3].split(' ')[0]:
# 	        	if row[0] in submission_emails:
# 		        	if row[2] not in submission_emails[row[0]]:
# 		        		submission_emails[row[0]].append(row[2])
# 	        		# print critical_questions[row[2].split(' ')[0]+' '+row[2].split(' ')[1]], row[3].split(' ')[0]
# 		    			print row
# 		    			submission_count+=1
# 		    	else:
# 		    		submission_emails[row[0]] = []
#         			# print row[]
#         	# print row
#     print submission_count