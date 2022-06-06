def simp(path):
    # split string by . .. or /
    # mulitple "/" are treated as one /
    # if ".."" encountered, go back one slash
    #    ex: /home/tool/../ equals response /home/tool

    # this shit wrong :(

    answer = ""
    slash = False
    last = False
    sec_con = False
    slash_pos = []

    for i in range(0, len(path) - 1):
        if sec_con is True:
            sec_con = False
            continue
        if path[i] != '/'and slash is True:
            slash = False
        if slash == True:
            continue
        if path[i] == '/':
            slash = True
            answer += path[i]
            slash_pos.append(i)
            continue
        if path[i] == '.' and path[i + 1] == '.' and path[i + 2] != '.':
            # delete previous instance up to second occur of "/"
            if len(slash_pos) > 1:
                answer = answer[:slash_pos[-2]]
            else:
                answer = "/"
            sec_con = True
            continue
        if (path[i] == '.' and path[i+1] != '.') and path[i+1] == '/':
            # condition to show current (last) location
            last = True
        answer += path[i]

    if last is True:
        answer = '/' + answer[slash_pos[-2]:]
        
    return answer


path = "/a/./b/../../c/"
print(simp(path))