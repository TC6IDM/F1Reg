import fastf1

def main():
    
    fastf1.Cache.enable_cache('./fastf1_cache')

    race = fastf1.get_session(2021, "Abu Dhabi Grand Prix", 'R')
    race.load()

    print(f"Event {race.event}")

    print(race.results)
    
if __name__ == '__main__':
    main()