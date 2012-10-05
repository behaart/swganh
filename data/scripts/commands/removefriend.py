import re
import swgpy
from swgpy.command import BaseSwgCommand

class RemoveFriendCommand(BaseSwgCommand):
    def run(self):
        split = re.split('\W+', self.getCommandString())
        friend_name = split[0]
        actor = self.getActor()
        player = actor.getPlayer()
        if player:
            # Check if the name is already our friend
            if player.isFriend(friend_name):
                player.removeFriend(friend_name)
                actor.sendSystemMessage(swgpy.outOfBand('cmnty', 'friend_removed', swgpy.ProseType.TT, friend_name), False, False)
            else:
                actor.sendSystemMessage(swgpy.outOfBand('cmnty', 'friend_not_found', swgpy.ProseType.TT, friend_name), False, False)
