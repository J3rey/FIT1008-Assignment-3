from landsites import Land

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
        selected_sites = []
        remaining_adventurers = self.adventurers

        # Calculate the number of adventurers to send to each land site
        num_sites = len(self.sites)
        if num_sites == 0:
            return selected_sites

        adventurers_per_site = remaining_adventurers // num_sites
        extra_adventurers = remaining_adventurers % num_sites

        # Select sites and assign adventurers
        for i, site in enumerate(self.sites):
            if extra_adventurers > 0:
                assigned_adventurers = adventurers_per_site + 1
                extra_adventurers -= 1
            else:
                assigned_adventurers = adventurers_per_site
            
            selected_sites.append((site, assigned_adventurers))

        return selected_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        rewards = []
        
        # Iterate over each configuration of adventurer numbers
        for num_adventurers in adventure_numbers:
            total_reward = 0
            remaining_adventurers = num_adventurers
            
            # Sort sites by gold in descending order
            sorted_sites = sorted(self.sites, key=lambda site: site.gold, reverse=True)
            
            # Allocate adventurers to sites to maximize reward
            for site in sorted_sites:
                if remaining_adventurers > 0:
                    total_reward += site.gold
                    remaining_adventurers -= 1
                else:
                    break

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
