class Solution:
    def trap(self, height: List[int]) -> int:
        suffix_max_array=height.copy()
        current_max=0
        for r_i in range(len(height)-1,-1,-1):
            if suffix_max_array[r_i]<current_max:
                suffix_max_array[r_i]=current_max
            else:
                current_max=suffix_max_array[r_i]
        total_water = 0
        current_max = 0
        for l_i,h in enumerate(height):
            if current_max<h:
                current_max=h
            else:
                total_water +=min(current_max,suffix_max_array[l_i])-h
        return total_water

