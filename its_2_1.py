routes = [[
    [1, 2, 5, 8, 9]
    , [1, 3, 6, 9]
    , [1, 4, 7, 6, 9]
    , [1, 4, 7, 9]]

    , [
        [1, 2, 5, 6, 8]
        , [1, 3, 6, 8]
        , [1, 4, 7, 9, 8]]

    , [
        [5, 6, 7]
        , [5, 8, 9, 7]]]

# sizes = [2448, 1224, 1112]
sizes = [3748, 1874, 3712]
# sizes = [3748, 1874, 912]
v_transfer = 200
t_comm = 1

min_uk_counts = [4, 4, 3]
block_packet_size = 100
t_transfer_block_packet = block_packet_size / v_transfer

time_lables = dict()
time_lable_routes = list()

counter = 0
for Route in routes:
    t_transfer = sizes[counter] / v_transfer
    counter += 1
    time_lable_routes.append(list())
    for route in Route:
        time_lable_routes[-1].append(list())
        t_current = 0
        for uk in route:
            t_current += t_comm

            if time_lables.get(uk):
                for time_lable in time_lables[uk]:
                    if abs(round(t_current - time_lable, 9)) < t_comm:
                        t_current = time_lable + t_comm
            else:
                time_lables[uk] = list()

            time_lables.get(uk).append(round(t_current, 9))
            time_lable_routes[-1][-1].append(round(t_current, 9))

            t_current += t_transfer

for Route, time_lable_Route, min_uk_count, size in zip(routes, time_lable_routes, min_uk_counts, sizes):
    t_transfer = size / v_transfer
    t_max = 0
    for route, time_lable_route in zip(Route, time_lable_Route):
        for uk, time_lable_uk in zip(route, time_lable_route):
            print(": ".join([str(uk), str(time_lable_uk)]))
            if time_lable_uk > t_max:
                t_max = time_lable_uk
        print("---------------------------------------")
    print(" ".join(["t comm =", str(t_comm)]))
    print(" ".join(["t transfer =", str(t_transfer)]))
    print(" ".join(["t max =", str(t_max)]))
    print(" ".join(["min uk count =", str(min_uk_count)]))
    t_all_block_packet = round((min_uk_count * 2 - 1) * t_comm + (min_uk_count - 1) * 2 * t_transfer_block_packet, 9)
    print(" ".join(["t block packet =", str(t_all_block_packet)]))
    print(" ".join(["t datagram = t max =", str(t_max)]))

    t_virtual_call = round(t_max + t_all_block_packet + t_comm, 9)
    print(" ".join(
        ["t virtual call =", str(t_max), '+', str(t_all_block_packet), '+', ''.join([str(t_comm), "(time for resort)"]),
         '=', str(t_virtual_call)]))

    print(" ".join(
        ["t virtual channel =", str(t_comm), '+', '(',
         str(t_transfer),
         '+', str(t_comm), ')', '*', '(', str(min_uk_count - 1), '+', str(len(Route) - 1), ')', '+',
         str(t_all_block_packet), '=',
         str(round(t_comm + (t_comm + t_transfer) * (min_uk_count - 1 + len(Route) - 1) + t_all_block_packet,
                   9))]))
    print(" ".join(
        ["t virtual channel veronica formul =", str(t_all_block_packet), '+', '(',
         str(t_transfer), '+', str(t_comm), ')', '*', '(', '3', '+', str(len(Route) - 1), ')', '+', str(t_comm), '=',
         str(round(t_all_block_packet + (t_comm + t_transfer) * (3 + len(Route) - 1) + t_comm,
                   9))]))
    print("---------------------------------------")
    print(end="\n\n")
