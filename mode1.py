from landsites import Land
from data_structures.heap import MaxHeap

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Best Case is O(1) if one or no landsites were added
        Worst Case is O(N*log(N)) where N is the number of land sites and log(N) is the complexity per insertion operation in a heap
        """
        self.sites = sites # Stores a list of 'Land' data classes
        self.adventurers = adventurers 
        self.site_heap = MaxHeap(len(sites)) # Initialises MaxHeap with the length of sites, used to maintain land sites based on gold to guardian ratio

        for site in sites: # Iterates through the 'Lands'
            ratio = site.get_gold() / site.get_guardians() # Calculates the gold to guardian ratio
            self.site_heap.add((ratio, site)) # Adds to the MaxHeap, with ratio as the key to be utilised by the MaxHeap and have site as the value

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Best Case is O(log(N)) where N is the number of land sites, as when the initial number of 
        adventurers is less than or equal to the guardians of the first/best site, only one extraction 
        and allocation is needed. log(N) is the height of the heap and the sinking operation takes
        O(log(N)) time.
        Worst Case is O(N) where N is the number of land sites, as when all the the adventurers 
        have to be distributed linearly across multiple sites until all adventurers are distributed
        """

        selected_sites = [] # Initialise an empty list to store [land and adventurers]
        remaining_adventurers = self.adventurers

        heap = MaxHeap(len(self.sites)) # Initialises another Maxheap to ensure that the original list of sites remain unchanged
        for site in self.sites:
            ratio = site.get_gold() / site.get_guardians()
            heap.add((ratio, site))

        while remaining_adventurers > 0 and len(heap) > 0: # Keep looping when there are still adventurers and Lands remaining
            ratio, best_site = heap.get_max() # Extracts Land with the largest gold to guardian ratio
            max_adventurers_for_site = min(best_site.get_guardians(), remaining_adventurers) # Allocates the adventurers to the amount of guardians of the Land
            selected_sites.append((best_site, max_adventurers_for_site)) # Append to selected_sites 
            remaining_adventurers -= max_adventurers_for_site # Subtract the adventurers that was just allocated from the remaining adventurers

        return selected_sites # Return List

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Both best and worst case O(A * N) where A is the length of adventure_numbers and N is the number 
        of sites, as it has to loop through all the sites and adventurers.
        As there is no early termination process the best and worst case are the same
        """
        rewards = [] # Initialise an empty list to store the rewards

        for num_of_adventurers in adventure_numbers: # For each number of adventurers in adventure_numbers
            self.adventurers = num_of_adventurers # set adventurers as the current number of adventurers in adventurenumbers
            calculated_reward = 0
            for site, adventurers_sent in self.select_sites(): # For each site that had already been distributed the number of adventurers 
                calculated_reward += min(adventurers_sent * site.get_gold() / site.get_guardians(), site.get_gold()) # Calculate the reward from the current site and add it to the total reward for configuration
            rewards.append(calculated_reward) # Append the calculated rewards onto rewards list

        return rewards # Return list of calculated rewards

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Best and Worst Case is O(1) as it updates the new reward and guardian value of the site in constant time
        """
        land.set_gold(new_reward) # Update selected site with new reward am
        land.set_guardians(new_guardians) # Update selected site with new guardian am

