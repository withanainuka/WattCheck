import matplotlib.pyplot as plt

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

energy_use = [
    884, 810, 740, 680,
    670, 730, 820, 790,
    650, 680, 730, 818
]

print("Home Energy Usage\n")

for i in range(len(months)):
    print(months[i], "-", energy_use[i], "kWh")

annual_use = sum(energy_use)
average_use = annual_use / len(energy_use)

highest_use = max(energy_use)
lowest_use = min(energy_use)

highest_month = months[energy_use.index(highest_use)]
lowest_month = months[energy_use.index(lowest_use)]

print("\nEnergy Summary")
print("Annual electricity use:", annual_use, "kWh")
print("Average monthly use:", round(average_use, 1), "kWh")
print("Highest-use month:", highest_month, "-", highest_use, "kWh")
print("Lowest-use month:", lowest_month, "-", lowest_use, "kWh")

off_peak_rate = 0.098
mid_peak_rate = 0.157
on_peak_rate = 0.203

off_peak_percent = 0.65
mid_peak_percent = 0.175
on_peak_percent = 0.175

monthly_costs = []

for use in energy_use:
    off_peak_use = use * off_peak_percent
    mid_peak_use = use * mid_peak_percent
    on_peak_use = use * on_peak_percent

    cost = (
        off_peak_use * off_peak_rate
        + mid_peak_use * mid_peak_rate
        + on_peak_use * on_peak_rate
    )

    monthly_costs.append(cost)

print("\nEstimated Monthly TOU Energy Costs")

for i in range(len(months)):
    print(months[i], "- $", round(monthly_costs[i], 2))

annual_cost = sum(monthly_costs)

print("\nEstimated Annual TOU Energy Cost: $", round(annual_cost, 2))

highest_cost = max(monthly_costs)
lowest_cost = min(monthly_costs)

highest_cost_month = months[monthly_costs.index(highest_cost)]
lowest_cost_month = months[monthly_costs.index(lowest_cost)]

print("\nCost Summary")
print("Most expensive month:", highest_cost_month, "- $", round(highest_cost, 2))
print("Cheapest month:", lowest_cost_month, "- $", round(lowest_cost, 2))

#First graph for Monthly electricity usage in kWh
plt.plot(months, energy_use, marker="o")

plt.title("Monthly Home Electricity Usage")
plt.xlabel("Month")
plt.ylabel("Electricity Use (kWh)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

#Second Graph for estimated monthly electricity cost
plt.bar(months, monthly_costs)

plt.title("Estimated Monthly Electricity Cost")
plt.xlabel("Month")
plt.ylabel("Cost ($)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()