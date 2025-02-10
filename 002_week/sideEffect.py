emoticon = "v.v"

def main():
  global emoticon
  say("Is there anyone?")
  emoticon = ":D"
  say("Oh! hi,")

def say(phrases):
  print(phrases + " " + emoticon)
  # this emoticon acess but not modify
  # if modify, use global keyword

main()