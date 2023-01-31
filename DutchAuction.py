import time
import signal

def DutchAuction(item, start, decrement, end=0, interval=5):

    """
    A Dutch Auction begins at a high price and gradually gets lower until the first bidder bids.
    The first bidder wins as opposed to a bidding war and last bidder wins. 

    item : the object up for auction.
    start : the starting auction price (for dutch auctions, it is a high stsrting price)
    decrement : how much will the price decrease every price change
    end : the end price for the auction, default is zero
    intervals : the amount of time that the price stays at a price level, default 5 seconds
    """

    def handle_timeout(signum, frame): #This function times the interval for each price level
        raise Exception("Time's Up!")

    price = start
    final_price = end
    next = None

    while next == None:
        print(f"\n\nWelcome to the auction for this {item}! \n")
        time.sleep(2)
        print(f"The starting price for this {item} is ${start}.\n")
        time.sleep(2)
        print(f"The final price will be ${end}.\n")
        time.sleep(2)
        print(f"Every {interval} seconds, the price will decrease by ${decrement}.\n") 
        time.sleep(2)
        print(f"Type 'bid' to bid.\n")
        time.sleep(1)
        print("Press Enter to continue.")
        nex = input()
        next = nex

    


    print("The auction begins in:")
    time.sleep(1)
    countdown  = 5
    while countdown > 0:
        print(countdown)
        time.sleep(1)
        countdown -= 1
    print("Let's Go!\n")

    
    while price >= final_price:
        print(f"    ${price}" )
        signal.signal(signal.SIGALRM, handle_timeout) #signal to end try bid input
        signal.alarm(interval) #start alarm
        try: #if user does not bid, the price will decrease to the next level
            bid = input()
        except Exception as e:
            if str(e) == "Time's Up!":
                signal.alarm(0) # end alarm
                price -= decrement
                continue
        signal.alarm(0)
        if bid == "bid":
            print(f"Congratulations! You have won the {item} for ${price}.")
            break
        price -= decrement
    if bid == None:
        print(f"Welp! Looks like no one wanted the {item}." )

#simple_MDA("baguette", 500, 10, 100, 2)
