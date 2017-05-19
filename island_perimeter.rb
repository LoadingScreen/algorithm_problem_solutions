# https://leetcode.com/problems/island-perimeter/#/description

"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

# @param {Integer[][]} grid
# @return {Integer}
def island_perimeter(grid)
    count = 0
    i = 0
    while i < grid.size
        j = 0
        while j < grid[0].size
            if grid[i][j] == 1
                if i > 0
                    count += (grid[i-1][j] != 1 ? 1 : 0)
                else
                    count += 1
                end
                if i < grid.size - 1
                    count += (grid[i+1][j] != 1 ? 1 : 0)
                else
                    count += 1
                end
                if j < grid[0].size - 1
                    count += (grid[i][j+1] != 1 ? 1 : 0)
                else
                    count += 1
                end
                if j > 0
                    count += (grid[i][j-1] != 1 ? 1 : 0)
                else
                    count += 1
                end
            end
            # p count
            j += 1
        end
        i += 1
    end
    count
end

