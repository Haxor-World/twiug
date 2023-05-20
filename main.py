import sys
import requests
import re
import time
import os


#__author__      = "Jevil36239"
#__github__      = "github.com/Jevil36239"
#__Finished__    = "20 - Mei - 2023"
#__name__        = "Twitter Username Grabber"


banner = f"""
            .-""-.            
     ______/      \         
    |______        ;    
           \      /     
            '-..-'        
       \         /   
        \ O  O /
         \_\_/_/     
           |~| 
          / ~ \\
         /_/ \_\      Twitter Username Grabber  
      __________________________
"""


def scrape_twitter_users(search_query):
    sImboLik_tWtitEr = "https://twitter.com/i/search/typeahead.json"
    hEaDDEER = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    PRAAAAAAMMmm_parameters = { # orr just https://twitter.com/i/search/typeahead.json?count=50&filters=true&include_entities=&lang=en&q=&result_type=users
        "count": "50",
        "filters": "true",
        "include_entities": "false",
        "lang": "en",
        "q": search_query,
        "result_type": "users"
    }

    lu_response_gua_aman = requests.get(sImboLik_tWtitEr, headers=hEaDDEER, params=PRAAAAAAMMmm_parameters)
    if lu_response_gua_aman.status_code == 200:
        UserRS = []
        data = lu_response_gua_aman.json()["users"]

        for user in data:
            username = re.sub(r"@(.*)", r"\1", user["screen_name"])
            UserRS.append(username)

        return UserRS
    else:
        print("- Error: Get None Results ")

def clear():
  os.system('clear')


def search_twitter_users():
    while True:
        clear()
        print(banner)
        print("\n| > 1. Single search\n| > 2. Multiple searches\n| > 3. Exit")
        choaice = input("{|} Select your Need : ")
        if choaice == "1":
            search_query = input("| > Enter search query {: ")
            UserRS = scrape_twitter_users(search_query)
            if UserRS:
                print("\nResults for '{}':\n".format(search_query))
                for user in UserRS:
                    print(user)
            else:
                print("\nNo results found for '{}'.".format(search_query))
        elif choaice == "2":
            keyword_file = input("| > Enter filename {: ")
            try:
                with open(keyword_file, "r") as f:
                    keywords = f.read().splitlines()
            except FileNotFoundError:
                print("Error: File not found.")
                continue
            for keyword in keywords:
                UserRS = scrape_twitter_users(keyword)
                if UserRS:
                    print("\nResults for '{}':\n{} | {:,}".format(keyword, "-" * len(keyword), len(UserRS)))
                    for user in UserRS:
                        print(user)
                else:
                    print("\n- Error: Got None Results from '{}'.".format(keyword))
        elif choaice == "3":
            break
        else:
            print("- Wrong Choice -")
            time.sleep(1)
            clear()


if __name__ == "__main__":
    search_twitter_users()
