import twint

c = twint.Config()
c.Username = "Username"
c.Search = "search"
c.Filter_retweets = True
c.All
c.Store_json = True
c.Output = "text.json"

twint.run.Search(c)
