import json, requests
import oauth2 as oauth
import os

# Customer keys & secret
CONSUMER_KEY = "INSERT HERE";
CONSUMER_SECRET = "INSERT HERE";
ACCESS_KEY = "INSERT HERE";
ACCESS_SECRET = "INSERT HERE";

def main():
    # prompt user for input
    query = input("What would you like to search for: ");
    lang = input("Return only from specific country: ");
    output = input("Whould you like to ouput tweets to a file: (/home/)");

    # clear terminal
    os.system("clear");

    # review selected options
    print ("Please review your selected options below:");
    print ("Search Twitter for: %s" %(query));
    if (lang == ""):
        print ("No country filter set...");
    else:
        print ("Country filter: %s" %(lang));
    print ("Outputting result to: %s" %(output));

    # wait for user
    input("Pess ENTER to continue...");

    # searching
    print("Searching....");
    queryTwitter(query, lang, output);

def OutputToFile(output, text):
    mode = 'a' if os.path.exists(output) else 'w'
    with open(output, mode) as f:
        f.write(text);
    f.close();

def queryTwitter(query, lang, output):
    req = "https://api.twitter.com/1.1/search/tweets.json?";

    # build request - better way of doing this needed... This will do for now.
    req += "q=" + query;
    if (lang.lower() != ""):
        req += "&" + lang;

    print("Requesting: %s" %(req));

    # query twitter
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET);
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET);
    client = oauth.Client(consumer, access_token);

    response, data = client.request(req);
    tweets = json.loads(data.decode('utf-8'));

    # check if user wants ouput
    if (output.lower() != ""):
        OutputToFile(output, tweets); # need to ouput important lines at top of file

    # pass output to be printed
    printIt(tweets);

def printIt(result):
    #print(result); -- debug
    print("Tweets found: " + result['search_metadata']['count']);
    # add top 5 tweets.
    print("Compiled in %s secounds..." %(result['search_metadata']['completed_in']));


if __name__ == "__main__":
    main();