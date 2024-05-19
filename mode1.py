from landsites import Land
from data_structures.heap import MaxHeap



class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Best Case is O(1)...
        Worst Case is O(n)...
        """
        self.sites = sites
        self.adventurers = adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        #less test cases, but correct complexities
        selected_sites = []
        num_sites = len(self.sites)
        if num_sites == 0:
            return selected_sites

        remaining_adventurers = self.adventurers
        heap = MaxHeap(num_sites)

        # Add all sites to the heap
        for site in self.sites:
            ratio = site.get_gold() / site.get_guardians()
            heap.add((ratio, site))

        # Extract the best site (site with the highest gold-to-guardians ratio)
        if remaining_adventurers > 0 and len(heap) > 0:
            _, best_site = heap.get_max()
            max_adventurers_for_site = min(best_site.get_guardians(), remaining_adventurers)
            selected_sites.append((best_site, max_adventurers_for_site))
            remaining_adventurers -= max_adventurers_for_site

        # Process remaining sites linearly
        for site in self.sites:
            if remaining_adventurers == 0:
                break
            if site == best_site:
                continue
            max_adventurers_for_site = min(site.get_guardians(), remaining_adventurers)
            selected_sites.append((site, max_adventurers_for_site))
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
        for site in self.sites:
            if site.name == land.name:
                site.set_gold(new_reward)
                site.set_guardians(new_guardians)
                break
