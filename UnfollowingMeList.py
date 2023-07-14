import json, os, logging, datetime
import pandas as pd

output = 'Output/'
logs = 'Logs/'

if not os.path.exists(output):  os.makedirs(output)
if not os.path.exists(logs):  os.makedirs(logs)

following = open("following.json","r")
followers = open("followers.json","r")

following_json = json.load(following)
followers_json = json.load(followers)

def parse_json(json_file, phrase=0):
    curr_set = set()
    if phrase:
        for user in json_file[phrase]:
            curr_set.add(user['string_list_data'][0]['value'])
    else:
        for user in json_file:
            curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

startTime = datetime.datetime.today()
log_fn = logs + __file__.split('/')[-1].split('.')[0] + startTime.strftime("_%m%d%y.txt")
logging.basicConfig(level=logging.INFO, filename= log_fn,format='%(asctime)s %(levelname)s %(message)s')

if __name__ == '__main__':
    try:
        logging.info('Program Started')
        
        not_following = pd.DataFrame(parse_json(following_json, 'relationships_following') - parse_json(followers_json),columns=['Unfollowed You'])
        logging.info('%s not_following.shape',not_following.shape)
        
        not_following.to_csv(output+ 'IG_unfollowers'+ startTime.strftime("_%m%d%y")+'.csv',index=False)
        logging.info('File saved to output folder')
        
    except Exception as e:
        logging.info(e)