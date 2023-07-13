import json 
import pandas as pd

following = open("following.json","r")
followers = open("followers.json","r")

following_json = json.load(following)
followers_json = json.load(followers)

def parse_json(json_file, phrase):
    curr_set = set()
    for user in json_file[phrase]:
        curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

not_following = pd.DataFrame(parse_json(following_json, 'relationships_following') - parse_json(followers_json, 'relationships_followers'),columns=['Unfollowed You'])

not_following.to_csv('IG_unfollowers.csv',index=False)