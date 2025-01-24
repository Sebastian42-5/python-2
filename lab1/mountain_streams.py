def stream_mountain():
    
    initial_streams = int(input("Select a number of streams between 1 and 100:"))
    initial_flows = [int(input("Select the flow for each stream")) for _ in range(initial_streams)]
    streams = list(range(1, initial_streams - 1))

    while True:

        line = int(input("Do we 99 (split stream), 88 (merge stream) or 77? (reach the end of the mountain)"))

        if line == 77:
            break
        elif line == 88:
            number_stream = [int(input("Select the two streams to be merged together:")) for _ in range(2)]
            streams.remove(number_stream[1])
            initial_flows[number_stream[0]] += initial_flows[number_stream[1]]
        elif line == 99:
            number_stream, percent = int(input("Select the stream to be split:")), int(input("Enter the percentage of each of the two new streams:")) 
            current_value = streams.pop(number_stream - 1)
            streams.insert(number_stream - 1, current_value * percent / 100)
            streams.insert(number_stream, current_value * (100 - percent) / 100)

    print(len(streams))
    print(initial_flows[i] for i in range(len(initial_flows)))

stream_mountain()



    

    





