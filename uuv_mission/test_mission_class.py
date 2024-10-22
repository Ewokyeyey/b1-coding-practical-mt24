import dynamic

# mission = dynamic.Mission.from_csv('/Users/elianakwok/Documents/Oxford/Course/Year 3/B1/Scientific Coding/b1-coding-practical-mt24/data/mission.csv')
mission = dynamic.Mission.from_csv('data/mission.csv')
print(f"Cave Heights: {mission.cave_height}")
print(f"Cave Depths: {mission.cave_depth}")