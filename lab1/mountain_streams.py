def stream_mountain():
    
    initial_streams = int(input("Select a number of streams between 1 and 100: "))
    flows = [int(input(f"Select the flow for stream {i + 1}: ")) for i in range(initial_streams)]

    while True:

        stream_action = int(input("Do we 99 (split stream), 88 (merge stream) or 77? (reach the end of the mountain): "))

        if stream_action == 77:
            break
        elif stream_action == 88:

            first_stream = int(input("Select the first stream to be merged together: ")) - 1
            second_stream = int(input("Select the second stream to be merged together: ")) - 1

            flows[first_stream] += flows[second_stream]
            flows.pop(second_stream)

        elif stream_action == 99:

            stream = int(input("Select the stream to be split: ")) - 1
            percent = int(input("Enter the percentage of the first new stream: ")) 

            original_flow = flows[stream]
            first_new_flow = original_flow * percent / 100
            second_new_flow = original_flow * (100 - percent) / 100
            
            flows[stream] = first_new_flow
            flows.insert(stream + 1, second_new_flow)

    print(len(flows))
    for i, flow in enumerate(flows, start=1):
        print(f"{flow:.2f}")

stream_mountain()



    

    





