import twitter_pb2
import sys
import io

twitter = twitter_pb2.Tweets()
f = open("twitter.pb","rb")
twitter.ParseFromString(f.read())
f.close()
delete_count = 0
for tweet in twitter.tweets:
	if tweet.is_delete==1:
		delete_count+=1
print("Deleted Tweets",delete_count)

reply = 0
for tweet in twitter.tweets:
	if tweet.HasField("insert"):
		if tweet.insert.reply_to:
			reply+=1
print("Reply Number",reply)

user = {}
for tweet in twitter.tweets:
	if tweet.HasField("insert"):
		if tweet.is_delete == 0:
			if tweet.insert.uid in user.keys():
				user[tweet.insert.uid]+=1
			else:
				user[tweet.insert.uid]=1
i = 0
for key, value in sorted(user.iteritems(), key = lambda (k,v):(v,k), reverse = True):
	print "%s:%s"%(key, value)
	i += 1
	if i ==5:
		break