# call_logs = [
#     {"caller": "A", "receiver": "B", "duration": 2},
#     {"caller": "C", "receiver": "D", "duration": 4},
#     {"caller": "E", "receiver": "F", "duration": 1},
# ]


# def identify_call_drop_caller_details(ele):
#     if ele["duration"]<5:
#         return ele


# # print(list(filter(identify_call_drop_caller_details,call_logs)))

# print(list(filter(lambda ele:ele["duration"]<5,call_logs)))


#sentiment classification-(postive/negative/neutral)
reviews = [
    "Excellent customer service and quick resolution to my issue.",
    "Terrible wait times and poor support response.",
    "Good performance overall, though setup was a bit confusing.",
    "Excellent connectivity and smooth user experience.",
    "Terrible customer care — nobody responded for hours.",
    "Good service at a reasonable price point.",
    "Excellent response time and very helpful staff.",
    "Terrible billing system, got charged incorrectly twice.",
    "Good internet speed most of the time.",
    "Excellent value for money and top-notch support.",
    "Terrible app interface, difficult to navigate.",
    "Good support team, but took a bit longer than expected.",
    "Excellent upgrade experience, highly recommend.",
    "Terrible call quality and frequent disconnections.",
    "Good technical assistance, resolved my problem quickly.",
    "Excellent follow-up and proactive communication.",
    "Terrible experience with the technician who came late.",
    "Good installation service, but signal strength varies.",
    "Excellent clarity during calls and zero downtime.",
    "Terrible onboarding process, confusing and frustrating.",
]



#if excellent -> Positive, Terrible -> Negative, Good->Neutral


# def sentiment_classifier(review):
#     if "excellent" in review.lower():
#         return "positive"
#     elif "good" in review.lower():
#         return "neutral"
#     else:
#         return "negative"

# sentimient_list = list(map(sentiment_classifier,reviews))


# sentimient_freq_dict={}


# for sentiment in sentimient_list:
#     if sentiment in sentimient_freq_dict.keys():
#         sentimient_freq_dict[sentiment]=sentimient_freq_dict[sentiment]+1

#     else:
#         sentimient_freq_dict[sentiment]=1


# print(sentimient_freq_dict)






#discount for customers

def discount_price(customer_type):

    def premium_discount_price(price):
        return price*0.5
    
    def regular_discount_price(price):
        return price*0.8
    
    if customer_type=="premium":
        return premium_discount_price
    
    elif customer_type=="regular":
        return regular_discount_price
    

customer_type = "regular"
discount_fn=discount_price(customer_type)
print(discount_fn(10000))