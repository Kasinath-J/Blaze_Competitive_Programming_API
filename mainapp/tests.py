    # def validate_name(self,value):
    #     if value!=None and value.strip()!="": 
    #         return value

    #     raise serializers.ValidationError("Invalid name")
        
    # def validate_leetcode(self,value):
        
    #     if value=="" or value==None:
    #         return None

    #     payload = {
    #         "operationName": "getUserProfile",
    #         "variables": {
    #             "username": value
    #         },
    #         "query": "query  getUserProfile($username: String!) {     matchedUser(username: $username) {     languageProblemCount  {   languageName    problemsSolved    }    profile {    reputation      ranking    }    badges {    displayName    icon    }   tagProblemCounts {   advanced   {   tagName     problemsSolved  }   fundamental   {   tagName     problemsSolved  }   intermediate   {   tagName     problemsSolved  }   }    submitStats {      acSubmissionNum {        difficulty        count        submissions      }     }     }} "
    #     }
    #     res = requests.get(url='https://leetcode.com/graphql',
    #                     json=payload,
    #                     )
        
    #     res = res.json()
    #     if "errors" in res:
    #         raise serializers.ValidationError("Incorrect leetcode profile")

    #     return value

    # def validate_github(self,value):
        
    #     if value=="" or value==None:
    #         return None
        
    #     token = GITHUB_API
    #     headers = {
    #         "authorization": "Bearer {}".format(token)
    #     }
    #     url = f'https://api.github.com/users/{value}'
    #     res = requests.get(url,headers=headers)
    #     print(res.status_code)
    #     if res.status_code!=200:
    #         raise serializers.ValidationError("Incorrect github profile")
    #     return value

    # def validate_linkedin(self,value):

    #     if value=="" or value==None:
    #         return None
        
    #     api = Linkedin(LINKEDIN_EMAIL,LINKEDIN_PASSWORD)
    #     profile = api.get_profile(value)
    #     if profile=={}:
    #         raise serializers.ValidationError("Incorrect linkedin profile")
    #     return value

    # def validate_hackerrank(self,value):

    #     if value=="" or value==None:
    #         return None
        
    #     ua = random.choice(user_agent)
    #     headers= {
    #         'user-agent': ua,
    #     }
    #     res = requests.get("https://www.hackerrank.com/rest/contests/master/hackers/{}/profile".format(value),headers=headers)
    #     if res.status_code!=200:
    #         raise serializers.ValidationError("Incorrect hackerrank profile")
    #     return value

    # def validate_codechef(self,value):

    #     if value=="" or value==None:
    #         return None
        
    #     url = "https://www.codechef.com/users/{}".format(value)
    #     res = requests.get(url)
    #     html_doc = res.text
    #     soup = BeautifulSoup(html_doc, 'html.parser')
        
    #     name_in_webpage = soup.find_all("ul",class_="side-nav")

    #     if len(name_in_webpage)!=0:
    #         return value
    #     raise serializers.ValidationError("Incorrect codechef profile")       

    # def validate_codeforces(self,value):

    #     if value=="" or value==None:
    #         return None
        
    #     url = "https://codeforces.com/api/user.info?handles={}".format(value)
    #     res = requests.get(url)
    #     if res.status_code!=200:
    #         raise serializers.ValidationError("Incorrect codeforces profile")
    #     return value
    