
grp_uuid_pairs = {
    'uuid1': 1,
    'uuid2': 2,
    'uuid7': 7,
    'uuid3': 3,
    'uuid11': 11,
    'uuid0': 0,
    'uuid-1': -1,
    'uuid22': 22,
}

reversed_dict_by_grp_id = {k: v for k, v in reversed(sorted(grp_uuid_pairs.items(), key=lambda item: item[1]))}

print('reversed_dict_by_grp_id  = {}'.format(reversed_dict_by_grp_id))

for k, v in reversed_dict_by_grp_id.items():
    print('k = {}, v = {}'.format(k, v))