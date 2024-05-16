from landsites import Land
from data_structures.heap import MaxHeap


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.heap = MaxHeap(len(sites))  # Initialize the max heap with the size of a given sites list
        self.adventurers = adventurers  

        for site in sites:
            self.heap.add(site)  # Adds each Land object to the max heap

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_sites = []
        remaining_adventurers = self.adventurers

        # Calculate the number of adventurers to send to each land site
        num_sites = len(self.heap)
        if num_sites == 0:
            return selected_sites

        adventurers_per_site = remaining_adventurers // num_sites
        extra_adventurers = remaining_adventurers % num_sites

        # Select sites and assign adventurers
        while len(self.heap) > 0:
            site = self.heap.get_max()
            if extra_adventurers > 0:
                assigned_adventurers = adventurers_per_site + 1
                extra_adventurers -= 1
            else:
                assigned_adventurers = adventurers_per_site
            
            selected_sites.append((site, assigned_adventurers))
            remaining_adventurers -= assigned_adventurers

        return selected_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        rewards = []
        
        for num_adventurers in adventure_numbers:
            max_reward = 0
            for site in self.sites:
                reward = min((num_adventurers * site.reward) / site.guardians, site.reward)
                max_reward = max(max_reward, reward)
            rewards.append(max_reward)
        
        return rewards

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        land.reward = new_reward
        land.guardians = new_guardians
