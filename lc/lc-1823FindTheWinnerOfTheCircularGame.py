#lc-1823: Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n <= 1:
            return n
        
        # Initialize array of friends (1-based indexing in problem, 0-based in array)
        friend_array = [True] * n
        current_pointer = 0
        friends_left = n
        
        # Stop when only one friend remains
        while friends_left > 1:
            # Count k friends, including eliminated ones
            count = 0
            while count < k - 1:  # Count k-1 steps to land on the kth friend
                current_pointer = (current_pointer + 1) % n
                if friend_array[current_pointer]:
                    count += 1
            
            # Eliminate the kth friend
            friend_array[current_pointer] = False
            friends_left -= 1
            
            # Move to the next non-eliminated friend
            current_pointer = (current_pointer + 1) % n
            while not friend_array[current_pointer]:
                current_pointer = (current_pointer + 1) % n
        
        # Return the 1-based index of the last remaining friend
        for i in range(n):
            if friend_array[i]:
                return i + 1