file_name = input('Enter the email file:')
handle = open(file_name)
e_counter = dict()
#email_list = list()
most_count = None
most_email = None

for line in handle:
    if line.startswith("From:"):
        line = line.rstrip()
        e_line = line.split()
        email = e_line[1]
        e_counter[email] = e_counter.get(email,0)+1
    for email,count in e_counter.items():
        if most_count is None or count > most_count:
            most_email = email
            most_count = count
        #email_list.append(email)

#for email in email_list:
    #e_counter[email] = e_counter.get(email,0)+1



        
print(most_email, most_count)       