#Enter Python code here and hit the Run button.

import re

def filtermail(mail: str):
    
    """ this function takes in the string text mail and return a flag if it contains shared email or not"""
    
    # convert the mail to lowercase
    mail = mail.lower()
    pattern = r"(share\b|shared|email|share+)" # create a regex pattered to find words
    result = re.findall(pattern, mail)
    result = set(result)
    
    #modal_verbs = r"(can|could|may|might|must|ought|shall|should|will|would)"
    #modal_verb_re = re.findall(modal_verbs, mail)
    
    
    if ("email" in result) and ("shared" in result):
        
        # return a flag 1 indicating it was shared
        return 1
    
    elif ("email" in result) and ("share" in result):
        
        # return a flag 0 indicating it has not been shared
        return 0
            
    else:
        
        # return -1 indicateds it does not contain email nor share keywords
        return -1

    
# now let's test this function  

# sample mail in string format
tests  = ["Can I share your email",
"I will share your email",
"I shall share your email",
"I've shared your email",
"May I share your email",
"Should I share your email",
"I already shared the email",
"I've just shared your email",
"Am I allowed to share your email",
"Am I able to share your email",
"I am able to share your email",
"Will you help my friends if I share your email with them?"]        


for mail in tests:
    flag = filtermail(mail)
    
    # prints the mail and the flag it belongs to
    if flag == 1:
        print("{} : Student has shared".format(mail))
    elif flag == 0:
        print("{} : Student wants to know if can share".format(mail))
    else:
        print("{} : this mail does not contain stem share and email".format(mail))
    
    