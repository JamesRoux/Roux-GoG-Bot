import json
import re
import datetime

with open('json/researches.json') as research:
    research = json.load(research)

#
# Gotta map all these id's to their respective numbers
# mostly just to make things easier
#

id =                            0
researches_id =                 1
tree =                          2
tier =                          3
row =                           4
level =                         5
food =                          6
wood =                          7
ore =                           8
silver =                        9
duration =                      10
power =                         11
req_id_1 =                      12
req_value_1 =                   13
req_id_2 =                      14
req_value_2 =                   15
req_id_3 =                      16
req_value_3 =                   17
req_id_4 =                      18
req_value_4 =                   19
req_id_5 =                      20
req_value_5 =                   21
req_id_6 =                      22
req_value_6 =                   23
benefit_id_1 =                  24
benefit_value_1 =               25
benefit_id_2 =                  26
benefit_value_2 =               27
benefit_id_3 =                  28
benefit_value_3 =               29
benefit_id_4 =                  30
benefit_value_4 =               31
benefit_id_5 =                  32
benefit_value_5 =               33
loc_research_name_id =          34
loc_research_description_id =   35
loc_tree_name_id =              36
loc_tree_description_id =       37
expend_score =                  38
benefit_score =                 39

def get_data(command):
    #
    # Regex for the short terms, i.e. "efp1"
    #
    if re.search(r"efp1", command):
        time = str(datetime.timedelta(seconds=int(research["900001"][duration])))
        response = "Food: " + research["900001"][food] + "\tWood: " + research["900001"][wood] + "\tIron: " + research["900001"][ore] + "\tSilver: " + research["900001"][silver] + "\tTime: " + time
        return response

    #
    # Regex for the full terms, i.e. "economy food production one"
    #
    if re.search("(\w*economy\w*)", command):
        if re.search("(\w*food production\w*)", command):
            if re.search("(\w*one|1\w*)", command):
                time = str(datetime.timedelta(seconds=int(research["900001"][duration])))
                response = "Food: " + research["900001"][food] + "\tWood: " + research["900001"][wood] + "\tIron: " + research["900001"][ore] + "\tSilver: " + research["900001"][silver] + "\tTime: " + time
                return response

    if re.search("(\w*development\w*)", command):
        response = "Yeah, i found the development label yay"
        return response

    if re.search("(\w*combat\w*)", command):
        response = "Yeah, i found the combat label yay"
        return response

    if re.search("(\w*combat2\w*)", command):
        response = "Yeah, i found the combat2 label yay"
        return response

    if re.search("(\w*defense\w*)", command):
        response = "Yeah, i found the defense label yay"
        return response

    if re.search("(\w*creation\w*)", command):
        response = "Yeah, i found the creation label yay"
        return response

    else:
        response = "Unfortunately, I dont know that research"
        return response
