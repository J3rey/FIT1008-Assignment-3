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
        self.sites = sites
        self.adventurers = adventurers
        self.site_heap = MaxHeap(len(sites))

        for site in sites:
            ratio = site.get_gold() / site.get_guardians()
            self.site_heap.add((ratio, site))

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Best Case is O(log(N)) where N is the number of land sites, as when the initial number of 
        adventurers is less than or equal to the guardians of the first/best site, only one extraction 
        and allocation is needed. log(N) is the height of the heap and the sinking operation takes
        O(log(N)) time.
        Worst Case is O(N) where N is the number of land sites, as when all the the adventurers 
        have to be distributed linearly across multiple sites until all adventurers are distributed
        """
        #less test cases, but correct complexities
        selected_sites = []
        remaining_adventurers = self.adventurers

        while remaining_adventurers > 0 and len(self.site_heap) > 0:
            # Extract the best site (site with the highest gold-to-guardians ratio)
            _, best_site = self.site_heap.get_max()
            max_adventurers_for_site = min(best_site.get_guardians(), remaining_adventurers)
            selected_sites.append((best_site, max_adventurers_for_site))
            remaining_adventurers -= max_adventurers_for_site

        return selected_sites


    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        rewards = []

        for num_adventurers in adventure_numbers:
            total_reward = 0
            remaining_adventurers = num_adventurers

            # Create a MaxHeap based on the gold values of the sites
            heap = MaxHeap(len(self.sites))

            for site in self.sites:
                heap.add((site.get_gold(), site))

            # Allocate adventurers to sites to maximize reward
            while remaining_adventurers > 0 and len(heap) > 0:
                gold, site = heap.get_max()
                total_reward += gold
                remaining_adventurers -= 1

            rewards.append(total_reward)

        return rewards

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        index = self.site_heap.index_map.get(land.name)
        if index is not None:
            # Update the site’s reward and guardians
            self.sites[index - 1].set_gold(new_reward)
            self.sites[index - 1].set_guardians(new_guardians)
            new_ratio = new_reward / new_guardians

            # Update the element in the heap and re-adjust
            self.site_heap.update_element(index, (new_ratio, self.sites[index - 1]))

