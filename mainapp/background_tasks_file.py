import requests
from background_task import background
import datetime
from .scraper.retreive import Leetcode_retreive_fn,Github_retreive_fn,Hackerrank_retreive_fn,Codechef_retreive_fn,Codeforces_retreive_fn,Problems_retreive_fn,Contest_retreive_fn
from cpapi.settings import BLAZE_BACKEND_URL

# For development server
base_url = BLAZE_BACKEND_URL+"update/"

# For production server
# base_url = BLAZE_BACKEND_URL+":8000/update/"

cur_Date = datetime.datetime.now(datetime.timezone.utc).date().strftime("%Y-%m-%d")

def retrieve_and_put_reqest_for_profiles(profile):
    ret = {
        "id":profile["id"],
        "name":profile["name"],
        "leetcode":None,
        "github":None,
        "linkedin":None,
        "hackerrank":None,
        "codechef":None,
        "codeforces":None,
    }
    try:
        if profile["leetcode"]==None or profile["leetcode"]=="":
            ret["leetcode"] = None 
        else:

            if ("leetcode_date" not in profile) or (profile["leetcode_date"]!=cur_Date):
                ret["leetcode"] = Leetcode_retreive_fn(profile["leetcode"])
    except:
        pass

    try:
        if profile["github"]==None or profile["github"]=="":
            ret["github"] = None 
        else:

            if ("github_date" not in profile) or (profile["github_date"]!=cur_Date):
                ret["github"] = Github_retreive_fn(profile["github"])    
    except:
        pass

    # try:
        # if profile["linkedin"]==None or profile["linkedin"]=="":
        #     ret["linkedin"] = None 
        # else:

        #     if ("linkedin_date" not in profile) or (profile["linkedin_date"]!=cur_Date):
        #         ret["linkedin"] = linkedin_scratch(profile["linkedin"])    
    # except:
    #     pass

    try:
        if profile["hackerrank"]==None or profile["hackerrank"]=="":
            ret["hackerrank"] = None 
        else:

            if ("hackerrank_date" not in profile) or (profile["hackerrank_date"]!=cur_Date):
                ret["hackerrank"] = Hackerrank_retreive_fn(profile["hackerrank"])    
    except:
        pass

    try:
        if profile["codechef"]==None or profile["codechef"]=="":
            ret["codechef"] = None 
        else:

            if ("codechef_date" not in profile) or (profile["codechef_date"]!=cur_Date):
                ret["codechef"] = Codechef_retreive_fn(profile["codechef"])    
    except:
        pass

    try:
        if profile["codeforces"]==None or profile["codeforces"]=="":
            ret["codeforces"] = None 
        else:

            if ("codeforces_date" not in profile) or (profile["codeforces_date"]!=cur_Date):
                ret["codeforces"] = Codeforces_retreive_fn(profile["codeforces"])    
    except:
        pass

    requests.put(base_url+"user/{}/".format(profile["id"]) ,json=ret)

def retrieve_and_put_reqest_for_contests_and_problems(data):
    ret={
        "total_easy":614,
        "total_medium":1335,
        "total_hard":556,
        "easy":{},
        "medium":{},
        "contest":{},
        "weekly_contest_no":323,
        "biweekly_contest_no":93,
    }

    if data['date']==cur_Date:
        print("Problems and Contest info are already updated today")
        return

    try:
        (ret['total_easy'],ret['total_medium'],ret['total_hard'],ret['problemsEasy'],ret['problemsMedium'])=Problems_retreive_fn(data['total_easy'],data['total_medium'],data['total_hard'])    
        (ret['contest'],ret['weekly_contest_no'],ret['biweekly_contest_no']) = Contest_retreive_fn(data['weekly_contest_no'],data['biweekly_contest_no'])

        requests.put(base_url+"problemscontest/",json=ret)

    except:
        return 


@background()
def main_background_fn():

    print("-----Updating Problems and Contest Info-----")
    problem_contest_res = requests.get(base_url+"problemscontest/")
    problem_contest_data = problem_contest_res.json()
    retrieve_and_put_reqest_for_contests_and_problems(problem_contest_data)
    
    print("------Updating Platform Info of All users------")
    profile_res = requests.get(base_url+"user/receiving_Data/")
    profiles = profile_res.json()

    for i in range(len(profiles)):
        print("Updating " + profiles[i]['id'] + " --> " + str(i+1) + " out of " + str(len(profiles)))
        retrieve_and_put_reqest_for_profiles(profiles[i])        


