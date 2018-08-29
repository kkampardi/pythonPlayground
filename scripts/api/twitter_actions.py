import twitter

consumer_key = 'pD6kZ95C84HvnFYEauIb11bW4'
consumer_secret = 'C2s3ghYeBEdPeLhimKYkwv7cDfIIl9zEoP4ZafrwrWn7jOYUgs'
access_token_key = '930157745705242626-QR9oyr6xCam2IVji9awRJjjFTirC03l'
access_token_secret = 'GeA27kCVtofgtoLth7rzpdIma86lccj73OATDXODg8TLe'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

# print(api.VerifyCredentials())

