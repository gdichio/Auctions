"""
The class auction will contain various auction models.

The MDA or Median Dutch Auction builds an infrastructure
for researchers to get paid for their contributions.
"""


class auction():
    
    def MDA(packet, copies=None, interest=None, 
            standby=None, length_auction=None, 
            scale_auction=None, start_value=None,
            end_value=None):
        """
        MDA stands for Median Dutch Auction. The auction 
        is for a specified amount of the object's (packet) 
        copies. If the user only submits the packet, they
        will automatically be in indefinite standby 
        until they configure the auction.

        The auction begins at a high price and decreases 
        at specified time intervals based on a model.
        The model would be calcualted with various 
        parameters and could be linear, rational etc.

        There would be a recommended model based on:
            type(packet);
            interest.
        But the auctioneer can engineer their own 
        auction instead of using the recommendation.

        As the auction progresses, there will be a 
        spread of buyer's transaction values. 
        The MDA finds the median value of all 
        transactions to build an equity model for the
        auctioneer and the buyers.

        There are three cases:
            A buyer pays more than the median
                - 100% equity in copy
                - M*value/median equity in original
                M : multiplier
                value : price paid
                median : median of auction
            A buyer pays the median
                - 100% equity in copy
                - 0% equity in original
            A buyer pays less than the median
                - L*value/median equity in copy
                L : multiplier
                value : price paid
                median : median of auction
                - 0% equity in original

        This provides a system where you can give credit
        to contributors and incentivise buyer's to 
        compensate contributors well to retain equity
        and gain equity in the original.

        There is also a time incentive to paying early.
        If you want to use the packet in your work, you
        may want a verified copy as soon as possible. 
        This would mean you would pay a higher price, 
        gain complete equity, and gain some equity in 
        the original.

        Note:   The median value is used opposed to the
                mean to avoid outliers.
                This stops an auctioneer from paying a 
                friend to buy a copy to boost the 
                average.

        """

        packet.type = "dict"
        # The packet is made of a modules or blocks.
        # These blocks consist of different info types.
        # The information will consist of the following
        # dict keys: Data, Image, Text, Constants
        #packet = {Absctract:"", Introduction:"", Data:[],
        #         Methods:"", Funding:0, Conclusion:"" } 

        copies.type = "int"
        # The copies variable is the number of verified
        # copies to auction.

        interest.type = "dict"
        # The interest variable is the amount of users
        # that are interested in the topic. 
        # The information will consist of the following
        # dict keys: type(User), Time-of-interest
        # interest = {Researchers:0, Funders:0,
        #             Pre-auction:0, Post-auction:0 } 
        
        standby.type = "int"
        # The standby variable is the amount of time
        # you would like to upload an open access version 
        # before auction.
        # This can help to gauge interest in the packet,
        # and find a good auction scale.

        length_auction.type = "int"
        # The auction length is the amount of time 
        # the auction takes in days.
        # auction_length = 0

        scale_auction.type = "list"
        # The auction scale is the way that the price
        # of the packet decreases in the auction. 
        # The items in the list include a model that 
        # describes the values per price drop, and a
        # value for the number of intervals between 
        # price drops.
        # auction_scale = ["model", 0]

        start_value.type = "int"
        # The start_value variable is the MDA's 
        # upper bound, or starting price.

        end_value.type = "int"
        # The end_value variable is the MDA's
        # lower bound, or ending price.

        pass
# %%
