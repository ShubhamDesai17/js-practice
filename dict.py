student_info={
    "name": "shubham",
    "class": "10",
    "age": "22"
}

print(student_info["name"])

# laptop={
#     "name":"hp",
#     "store":"pune"
# }

# print(laptop["name"])

ec2_instance_info=[
    {
        "id":"001",
        "type": "t2.micro"
    },

    {
        "id":"002",
        "type":"t2.medium"
    },
    {
        "id": "003",
        "type":"t3.xlarge"
    },
    {
        "id":"004",
        "type": "custome"
    }
]
print(ec2_instance_info[0]["id"])
print(ec2_instance_info[1]["type"])
print(ec2_instance_info[3]["id"])

