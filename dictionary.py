car={
    "model":"Toyota",
    "year":2020,
    "color":"Red"
}

x=car.get("model")

print(x)

# // Output: Toyota
# // Set Example

my_set={"anshu", "sacchin", "Kholi"}
my_set2={"anshu", "sacchin", "Kholi"}

my_set.add("Rohit")
my_set.remove("anshu")

result=my_set.union(my_set2)
# y="Anshu" in my_set


print(my_set)
# print(y)
print(result)
