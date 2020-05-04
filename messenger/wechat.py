import itchat

itchat.auto_login()

author = itchat.search_friends(name='Sean')[0]

author.send('Hello, filehelper')