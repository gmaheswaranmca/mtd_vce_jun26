n = int(input())
names = [s for s in input().split(' ')][:n]
def groupAnagrams(names):
    n = len(names)
    all_groups = []
    
    for I in range(n):
        if names[I] == '':
            continue 
        group = [names[I]]
        for J in range(I+1,n):
            if len(names[I]) != len(names[J]):
                continue
            if list(sorted(names[I])) == list(sorted(names[J])):
                group.append(names[J])
                names[J] = ''
        all_groups.append(group)
    return all_groups 
print(groupAnagrams(names))