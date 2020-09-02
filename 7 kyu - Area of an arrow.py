'''
Area of an arrow
An arrow is formed in a rectangle with sides a and b by joining the bottom corners to the midpoint of the top edge 
and the centre of the rectangle.

data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAEsCAYAAADtt+XCAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAABJwSURBVHhe7d0LsFVV/cDxhSCP0NBKTS1MDVPHNBnLNDRNLKPRCjNfaEU1ppWZlmNqoKZFD1PHfGSpkRlU09PsXU5WVCpiZJgvMh/ZQ5BEA0S8f37rvy+CD4Qfj3vOPZ/PDHPvPus2Nbd77/fsvfZeq0/XYgUAVtI6zUcAWCkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkBKn67Fms87ypw5c8rcuXObI4Cn169fv7LRRhvVjyyrYwOyxx57lMcff7wMHjy4fgR4soEDB5arr766zJ49u2y44YbNq3Tr6IBcc8013lUAyzVy5MgyadKkehbCsjp6DuTBBx9sPgN4egsWLGg+48lMogOQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAApAgIACkCAkCKgACQIiAAPWzs2LFl0aJFzVH7EBCAHnb55ZeXrq6u5qh9CAhAC/jf//5Xjj322HL++ec3r7Q+AQFoARtvvHHZddddy5VXXlle8IIXNK+2NgEBaAF33313Ofzww8sf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

a and b are integers and > 0

Write a function which returns the area of the arrow.
'''

def arrow_area(a, b):
    return (a * (b / 2)) / 2