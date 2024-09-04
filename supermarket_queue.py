import heapq

def queue_time(customers, n):
    # Create a list to represent the checkout tills
    tills = [0] * n
    
    # Use a heap (priority queue) to efficiently get the till with the minimum time
    heapq.heapify(tills)
    
    for time in customers:
        # Assign the customer to the till with the least time
        # Pop the smallest element (till that will be available the earliest)
        earliest_till = heapq.heappop(tills)
        
        # Add the customer's checkout time to this till's time
        earliest_till += time
        
        # Push the updated time back into the heap
        heapq.heappush(tills, earliest_till)
    
    # The total time required will be the maximum time in the tills list
    return max(tills)
            