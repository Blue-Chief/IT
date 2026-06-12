import math

while True:
    try:
        archive_size = int(input("Enter Size of Archive Size in GB: ").replace("GB", "").upper())
        break
    except ValueError as err:
        print(f"{err} Enter a Valid Number")

while True:
    try:
        volumes = int(input("Enter Volumes for Archive SIze to be Split: "))
        break
    except ZeroDivisionError as err:
        print(f"{err} Cannot Divide by Zero Enter a Valid Number")
    except ValueError as err:
        print(f"{err} Enter a Valid Number")

def calculate_volume_splitter(archive_size:int, volumes:int):
    volume_split = archive_size / volumes
    
    volume_split = math.ceil(volume_split)
    return volume_split    

if archive_size <= 10:
    archive_size = archive_size * 1024
    result = calculate_volume_splitter(archive_size, volumes)
    print(f"Size for each volume is {result} MB")
else:
    result = calculate_volume_splitter(archive_size, volumes)
    print(f"Size for each volume is {result} GB")