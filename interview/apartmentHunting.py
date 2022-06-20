def apartmentHunting(blocks, reqs):
    distance = []
    for i in range(len(blocks)):
        for j in reqs:
            near = float('inf')
            curr = 0
            if blocks[i][j]:
                print("True")
            else:
                
                    

blocks = [
{
    "gym": False,
    "school": True,
    "store": False,
},
{
    "gym": True,
    "school": False,
    "store": False,
},
{
    "gym": True,
    "school": True,
    "store": False,
},
{
    "gym": False,
    "school": True,
    "store": False,
},
{
    "gym": False,
    "school": True,
    "store": True,
}
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))
