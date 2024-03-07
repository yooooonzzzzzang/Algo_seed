def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:x[0])
    f_h, f_m =  book_time[0][1].split(":")
    f_t = int(f_h) * 60 + int(f_m)
    room = [[f_t]]

    for i in range(1, len(book_time)):
        
        in_h, in_m =  book_time[i][0].split(":")
        out_h, out_m =  book_time[i][1].split(":")
        in_time = int(in_h)* 60 + int(in_m)
        out_time = int(out_h)* 60 + int(out_m)
        
        for j in range(len(room)):
            if room[j][-1] + 10 <= in_time:
                room[j].append(out_time)
                break        
        else:room.append([out_time])
                    
    return len(room)