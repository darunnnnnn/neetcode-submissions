class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        people.sort()

        no = 0 

        a = 0 

        b = len(people) - 1 

        while a <= b : 

            if people[a] + people [b] <= limit : 

                no += 1 

                a += 1 
                b -= 1 

            elif people[a] + people[b] > limit : 

                no += 1 

                b -= 1 
        return no


        