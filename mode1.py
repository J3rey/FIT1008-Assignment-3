from landsites import Land


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sites
        self.adventurers = adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_sites = []
        remaining_adventurers = self.adventurers
        
        # Sort sites by the ratio of guardians to reward in ascending order
        sorted_sites = sorted(self.sites, key=lambda site: site.guardians / site.reward)
        
        for site in sorted_sites:
            if remaining_adventurers == 0:
                break
            if site.guardians <= remaining_adventurers:
                selected_sites.append((site, site.guardians))
                remaining_adventurers -= site.guardians
        
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
